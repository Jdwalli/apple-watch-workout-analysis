import xml.etree.cElementTree as ET
from werkzeug.datastructures import FileStorage
from zipfile import ZipFile
import os
import pandas as pd
import config

from parsers.activity_summary_parser import ActivitySummaryParser

class AppleHealthExportParser:
    def __init__(self, export_file: FileStorage):
        self.export_file = export_file
        self.export_file_path = "apple_health_export/"
        self.zipFile = ZipFile(self.export_file, "r")
        self._validate_apple_health_export()

        self.export_root = self._generate_root()

        self.health_export_file_path = os.path.join(self.export_file_path, "export.xml")
        self.workout_routes_directory_path = os.path.join(self.export_file_path, "workout-routes")
        self.electrocardiograms_directory_path = os.path.join(self.export_file_path, "electrocardiograms")


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
            raise RuntimeError(f"Exception occurred when trying to parse the tree root: {e}")

    def _parse_activity_summary_elements(self) -> None:
        activity_summary_path = os.path.join(config.HEALTH_ELEMENTS_DIRECTORY, "activity_summaries")
        self.activity_summaries = self.export_root.findall("ActivitySummary")
        parsed_activity_summaries = [
            ActivitySummaryParser(activity_summary).csv_row_structure()
            for activity_summary in self.activity_summaries
        ]

        df = pd.DataFrame(parsed_activity_summaries, columns=ActivitySummaryParser.ACTIVITY_SUMMARY_COLUMNS)
        df.to_csv(activity_summary_path, index=False, header=True)

    def _parse_workout_elements(self) -> None:
        return NotImplementedError

    def _parse_health_record_elements(self) -> None:
        return NotImplementedError

    def _parse_gpx_files(self) -> None:
        return NotImplementedError

    def parse_health_elements(self):
        self._parse_gpx_files()
        self._parse_health_record_elements()
        self._parse_activity_summary_elements()
        self._parse_workout_elements()
