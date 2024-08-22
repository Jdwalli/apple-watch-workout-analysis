import xml.etree.cElementTree as ET
from werkzeug.datastructures import FileStorage
from zipfile import ZipFile
import os
import pandas as pd
import config
from utils import name_utils as name_utils

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
        self.export_root = self._generate_root()

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

    def _generate_root(self) -> ET.Element:
        try:
            return ET.fromstring(self.zipFile.read(self.health_export_file_path))
        except Exception as e:
            raise RuntimeError(
                f"Exception occurred when trying to parse the tree root: {e}"
            ) from e

    def _parse_activity_summary_elements(self) -> None:
        activity_summary_path = os.path.join(
            config.HEALTH_ELEMENTS_DIRECTORY, config.ACTIVITY_SUMMARY_FILE_NAME)
        self.activity_summaries = self.export_root.findall("ActivitySummary")
        parsed_activity_summaries = [
            ActivitySummaryParser(activity_summary).csv_row_structure()
            for activity_summary in self.activity_summaries
        ]

        df = pd.DataFrame(parsed_activity_summaries,
                          columns=ActivitySummaryParser.ACTIVITY_SUMMARY_COLUMNS)
        df.to_csv(activity_summary_path, index=False, header=True)

    def _parse_workout_elements(self) -> None:
        parsed_workout_path = os.path.join(
            config.WORKOUT_ELEMENTS_DIRECTORY, config.WORKOUTS_SUMMARY_FILE_NAME)
        self.workouts = self.export_root.findall('Workout')

        parsed_workouts = [
            list(WorkoutRecordParser(workout).csv_row_structure())
            for workout in self.workouts
        ]

        df = pd.DataFrame(
            parsed_workouts, columns=WorkoutRecordParser.MASTER_WORKOUT_COLUMNS)
        df.to_csv(parsed_workout_path, index=False, header=True)

    def _parse_health_record_elements(self) -> None:
        self.records = self.export_root.findall('Record')
        records_data = {name_utils.remove_record_type_prefix(
            record.get("type")): [] for record in self.records}

        for record in self.records:
            current_record = HealthRecordParser(record)
            record_type = current_record.record_type
            record_data = current_record.csv_row_structure()

            records_data[record_type].append(record_data)

        for record in records_data:
            records_data[record] = pd.DataFrame(
                records_data[record], columns=HealthRecordParser.get_column_type(record))
            df = pd.DataFrame.from_dict(records_data[record])
            df.to_csv(os.path.join(config.HEALTH_ELEMENTS_DIRECTORY,
                      f"{record}.csv"), index=False, header=True)

    def _parse_gpx_files(self) -> None:
        gpx_file_paths = [
            file.filename
            for file in self.zipFile.infolist()
            if file.filename.startswith(self.workout_routes_directory_path)
        ]

        for gpx_file_path in gpx_file_paths:
            ns = {"gpx": "http://www.topografix.com/GPX/1/1"}
            tracks = ET.fromstring(self.zipFile.read(
                gpx_file_path)).findall('gpx:trk', ns)

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
