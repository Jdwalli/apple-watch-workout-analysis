"""
Parses Apple health workout data and converts it into CSV-compatible row structures.

This module provides the `WorkoutRouteParser` class, which is used to parse
tracks elements stored in a GPX format and convert them into a dataframe.

This module provides the `WorkoutRecordParser` class, which is used to parse
Workout elements stored in a xml format and convert them into tuples that can 
be exported to CSV files.

Usage example:
    workout_tracks = WorkoutRouteParser(tracks)
    df = workout_tracks.to_dataframe()

Usage example:
    workout = WorkoutRecordParser(workout)
    workout_csv_row = workout.csv_row_structure()
"""

import xml.etree.cElementTree as ET
from utils import name_utils as name_utils
from typing import List
import pandas as pd


class WorkoutRouteParser:
    WORKOUT_ROUTE_COLUMNS = [
        "lon",
        "lat",
        "elevation",
        "time",
        "speed",
        "course",
        "hAcc",
        "vAcc",
    ]

    def __init__(self, tracks: List[ET.Element]):
        """Initializes the WorkoutRouteParser with a tracks element.

        Args:
            tracks: A list of ET.Element representing track points.
        """
        self.ns = {"gpx": "http://www.topografix.com/GPX/1/1"}
        self.tracks = tracks
        self.workout_route_data = []

    def _get_track_segments(self, track: ET.Element) -> ET.Element:
        """Retrieves all track segments within a track element.

        Args:
            track: An XML element representing a track from a GPX file.

        Returns:
            A list of XML elements representing the track segments ('trkseg') 
            within the provided track element.
        """
        return track.findall('gpx:trkseg', self.ns)

    def _get_track_points(self, track_segment: ET.Element) -> ET.Element:
        """Retrieves all track points within a track element.

        Args:
            track: An XML element representing a track_segment from a GPX file.

        Returns:
            A list of XML elements representing the track points ('trkpt') 
            within the provided track element.
        """
        return track_segment.findall('gpx:trkpt', self.ns)

    def _extract_gpx_data(self) -> None:
        """Extracts data from GPX tracks and stores it in the workout_route_data list.

        This method iterates over each track, retrieves its segments, and then extracts
        data from each track point within those segments. The extracted data is converted
        into a CSV-compatible row structure and appended to the workout_route_data list.
        """

        for track in self.tracks:
            for track_segment in self._get_track_segments(track):
                for track_point in self._get_track_points(track_segment):
                    track_point_data = self._to_csv_row_structure(track_point)
                    self.workout_route_data.append(track_point_data)

    def _to_csv_row_structure(self, track_point: ET.Element) -> tuple:
        """Constructs a tuple representing the CSV row structure for a given track point.

        The units of the elements can be found at https://www.topografix.com/GPX/1/1/gpx.xsd




        Args:
            track_point: An XML element representing a track point ('trkpt') 
                        from a GPX file.

        Returns:
            A tuple containing the following elements extracted from the track point:
            - Longitude (lon)
            - Latitude (lat) 
            - Elevation (ele) (Meters)
            - Time (time)
            - Speed (speed) (Meters Per Second)
            - Course (course) (Decimal Degrees)
            - Horizontal Accuracy (hAcc) (Meters)
            - Vertical Accuracy (vAcc) (Meters)
        """
        elevation = track_point.find('gpx:ele', self.ns).text
        time = track_point.find('gpx:time', self.ns).text
        extension = track_point.find('gpx:extensions', self.ns)
        lon = track_point.get("lon")
        lat = track_point.get("lat")
        speed = extension.find('gpx:speed', self.ns).text
        course = extension.find('gpx:course', self.ns).text
        hAcc = extension.find('gpx:hAcc', self.ns).text
        vAcc = extension.find('gpx:vAcc', self.ns).text

        return (lon, lat, elevation, time, speed, course, hAcc, vAcc)

    def to_dataframe(self) -> pd.DataFrame:
        """Converts the extracted GPX data into a pandas DataFrame.

        This method calls the _extract_gpx_data method to populate the 
        workout_route_data list with  data from the GPX tracks. 
        It then converts this list into a pandas DataFrame, using the 
        WORKOUT_ROUTE_COLUMNS as the column.

        Returns:
            pd.DataFrame: A DataFrame containing the workout route data, with 
                          columns for longitude, latitude, elevation, time, 
                          speed, course, horizontal accuracy, and vertical accuracy.
        """
        self._extract_gpx_data()
        return pd.DataFrame(self.workout_route_data, columns=self.WORKOUT_ROUTE_COLUMNS)


class WorkoutRecordParser:
    def __init__(self):
        pass

    def csv_row_structure(self):
        pass
