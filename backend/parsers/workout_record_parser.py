"""
Parses Apple health workout data and converts it into CSV-compatible row structures.

This module provides the `WorkoutRouteParser` class, which is used to parse
trkpt (track point) elements stored in a GPX format and convert them into
tuples that can be exported to CSV files.

This module provides the `WorkoutRecordParser` class, which is used to parse
Workout elements stored in a xml format and convert them into tuples that can 
be exported to CSV files.

Usage example:
    trk_point = WorkoutRouteParser(track_point)
    trk_point_row = trk_point.csv_row_structure()

Usage example:
    workout = WorkoutRecordParser(workout)
    workout_csv_row = workout.csv_row_structure()
"""

import xml.etree.cElementTree as ET
from utils import name_utils as name_utils

class WorkoutRouteParser:
    def __init__(self, track_point: ET.Element):
        """Initializes the WorkoutRouteParser with an track_point element.

        Args:
            track_point: ET.Element representing a track point.
        """
        self.ns = {"gpx": "http://www.topografix.com/GPX/1/1"}
        self.track_point = track_point

    def csv_row_structure(self) -> tuple:
        """Returns the CSV row structure for the track_point

        Returns:
            A tuple representing the CSV row structure for the track_point.
        """
        elevation = self.track_point.find('gpx:ele', self.ns).text
        time = self.track_point.find('gpx:time', self.ns).text
        extension = self.track_point.find('gpx:extensions', self.ns)
        lon = self.track_point.get("lon")
        lat = self.track_point.get("lat")
        speed = extension.find('gpx:speed', self.ns).text
        course = extension.find('gpx:course', self.ns).text
        hAcc = extension.find('gpx:hAcc', self.ns).text
        vAcc = extension.find('gpx:vAcc', self.ns).text

        return (lon, lat, elevation, time, speed, course, extension, hAcc, vAcc)

class WorkoutRecordParser:
    def __init__(self):
        pass

    def csv_row_structure(self):
        pass