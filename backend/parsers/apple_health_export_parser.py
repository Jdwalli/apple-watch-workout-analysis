import xml.etree.cElementTree as ET
from werkzeug.datastructures import FileStorage
from zipfile import ZipFile
import os
import pandas as pd
import config

from utils import name_utils as name_utils
from utils import file_utils as file_utils

from parsers.activity_summary_parser import ActivitySummaryParser
from parsers.workout_record_parser import WorkoutRouteParser, WorkoutRecordParser
from parsers.health_record_parser import HealthRecordParser


class AppleHealthExportParser:
    def __init__(self, export_file: FileStorage):
        self.export_file = export_file
        self.export_file_path = "apple_health_export/"
        self.zipFile = ZipFile(self.export_file, "r")

        self.health_export_file_path = os.path.join(
            self.export_file_path, "export.xml")
        self.workout_routes_directory_path = os.path.join(
            self.export_file_path, "workout-routes")
        self.electrocardiograms_directory_path = os.path.join(
            self.export_file_path, "electrocardiograms")

        self._validate_apple_health_export()

    def _validate_apple_health_export(self):
        """Validates whether the provided file is a valid Apple Health export.

        This function checks the contents of the provided ZIP file to determine 
        if it contains the necessary files and types that identify it as an 
        Apple Health export. Specifically, it looks for specific filenames and 
        file types that are expected in an Apple Health export package.

        Raises:
            ValueError: If the file does not meet the criteria for an Apple Health export.
        """

        # TODO IMPLEMENT
        return True

    def _parse_activity_summary_elements(self) -> None:
        """Parses activity summary elements from the Apple Health export XML and writes them to a CSV file.

        This method opens the Apple Health export XML file within the ZIP archive, then iteratively parses
        the XML to find and process each 'ActivitySummary' element. Each parsed element is converted into
        a CSV-compatible row structure using the ActivitySummaryParser. The method accumulates these
        row structures into a list and, once all elements have been processed, writes the list to a CSV
        file at the specified path.
        """

        activity_summary_path = os.path.join(
            config.HEALTH_ELEMENTS_ACTIVITY_DIRECTORY, config.ACTIVITY_SUMMARY_FILE_NAME)
        parsed_activity_summaries = []

        with self.zipFile.open(self.health_export_file_path) as xml_file:
            for _, elem in ET.iterparse(xml_file, events=("end",)):
                if elem.tag == "ActivitySummary":
                    parsed_activity_summaries.append(
                        ActivitySummaryParser(elem).csv_row_structure()
                    )
                    elem.clear()

        df = pd.DataFrame(parsed_activity_summaries,
                          columns=ActivitySummaryParser.ACTIVITY_SUMMARY_COLUMNS)
        df.to_csv(activity_summary_path, index=False, header=True)

    def _parse_workout_elements(self) -> None:
        """Parses workout elements from the Apple Health export XML and writes them to a CSV file.

        This method opens the Apple Health export XML file within the ZIP archive, then iteratively parses
        the XML to find and process each 'Workout' element. Each parsed element is converted into
        a CSV-compatible row structure using the WorkoutRecordParser. The method accumulates these
        row structures into a list and, once all elements have been processed, writes the list to a CSV
        file at the specified path.
        """
        parsed_workout_path = os.path.join(
            config.WORKOUT_ELEMENTS_DIRECTORY, config.WORKOUTS_SUMMARY_FILE_NAME)
        parsed_workouts = []

        with self.zipFile.open(self.health_export_file_path) as xml_file:
            for event, elem in ET.iterparse(xml_file, events=("end",)):
                if elem.tag == 'Workout':
                    parsed_workouts.append(
                        list(WorkoutRecordParser(elem).csv_row_structure())
                    )
                    elem.clear()

        df = pd.DataFrame(
            parsed_workouts, columns=WorkoutRecordParser.MASTER_WORKOUT_COLUMNS)
        df.to_csv(parsed_workout_path, index=False, header=True)

    def _parse_health_record_elements(self) -> None:
        """Parses health record elements from the Apple Health export XML and writes them to a CSV file.

        This method opens the Apple Health export XML file within the ZIP archive, then iteratively parses
        the XML to find and process each 'Record' element. Each parsed element is converted into
        a CSV-compatible row structure using the HealthRecordParser. The method accumulates these
        row structures into a list and, once all elements have been processed, writes the list to a CSV
        file at the specified path.
        """
        records_data = {}

        with self.zipFile.open(self.health_export_file_path) as xml_file:
            for event, elem in ET.iterparse(xml_file, events=("end",)):
                if elem.tag == 'Record':
                    if elem.get('sourceName') != "Health":
                        record_type = name_utils.remove_record_type_prefix(
                            elem.get("type")
                        )
                        if record_type not in records_data:
                            records_data[record_type] = []

                        current_record = HealthRecordParser(elem)
                        records_data[record_type].append(
                            current_record.csv_row_structure()
                        )
                    elem.clear()

        for record_type, record_list in records_data.items():
            df = pd.DataFrame(
                record_list, columns=HealthRecordParser.get_column_type(record_type))
            df.to_csv(os.path.join(file_utils.match_record_type_to_directory(record_type),
                      f"{record_type}.csv"), index=False, header=True)

    def _parse_gpx_files(self) -> None:
        """Parses gpx files from the Apple Health export zip and writes them to a CSV file.
        """
        gpx_file_paths = [
            file.filename
            for file in self.zipFile.infolist()
            if file.filename.startswith(self.workout_routes_directory_path)
        ]

        for gpx_file_path in gpx_file_paths:
            ns = {"gpx": "http://www.topografix.com/GPX/1/1"}
            with self.zipFile.open(gpx_file_path) as gpx_file:
                tracks = ET.parse(gpx_file).getroot().findall('gpx:trk', ns)
                df = WorkoutRouteParser(tracks).to_dataframe()

            filename_without_extension, _ = os.path.splitext(
                os.path.basename(gpx_file_path))
            df.to_csv(os.path.join(config.WORKOUT_ROUTE_ELEMENTS_DIRECTORY,
                      f"{filename_without_extension}.csv"), index=False, header=True)

    def parse_health_elements(self):
        self._parse_gpx_files()
        self._parse_health_record_elements()
        self._parse_activity_summary_elements()
        self._parse_workout_elements()
