import unittest
from unittest.mock import MagicMock
import xml.etree.ElementTree as ET
from parsers.workout_record_parser import WorkoutRouteParser, WorkoutRecordParser
import config


class TestWorkoutRouteParser(unittest.TestCase):

    def setUp(self):
        self.track_point_mock = MagicMock(spec=ET.Element)
        self.track_segment_mock = MagicMock(spec=ET.Element)
        self.track_mock = MagicMock(spec=ET.Element)

        self.track_point_mock.get.side_effect = lambda x: {"lon": "12.34", "lat": "56.78"}.get(x)
        self.track_point_mock.find.side_effect = lambda x, ns: {
            "gpx:ele": MagicMock(text="100"),
            "gpx:time": MagicMock(text="2024-08-21T10:00:00Z"),
            "gpx:extensions": self._mock_extension()
        }.get(x)

        self.track_segment_mock.findall.return_value = [self.track_point_mock]
        self.track_mock.findall.return_value = [self.track_segment_mock]

        self.parser = WorkoutRouteParser(tracks=[self.track_mock])

    def _mock_extension(self):
        extension_mock = MagicMock(spec=ET.Element)
        extension_mock.find.side_effect = lambda x, ns: {
            "gpx:speed": MagicMock(text="10.5"),
            "gpx:course": MagicMock(text="90"),
            "gpx:hAcc": MagicMock(text="5"),
            "gpx:vAcc": MagicMock(text="2")
        }.get(x)
        return extension_mock

    def test_to_csv_row_structure(self):
        result = self.parser._to_csv_row_structure(self.track_point_mock)
        expected = ("12.34", "56.78", "100", "2024-08-21T10:00:00Z", "10.5", "90", "5", "2")
        self.assertEqual(result, expected)

    def test_extract_gpx_data(self):
        self.parser._extract_gpx_data()
        expected = [("12.34", "56.78", "100", "2024-08-21T10:00:00Z", "10.5", "90", "5", "2")]
        self.assertEqual(self.parser.workout_route_data, expected)

    def test_to_dataframe(self):
        df = self.parser.to_dataframe()
        expected_data = {
            "lon": ["12.34"],
            "lat": ["56.78"],
            "elevation": ["100"],
            "time": ["2024-08-21T10:00:00Z"],
            "speed": ["10.5"],
            "course": ["90"],
            "hAcc": ["5"],
            "vAcc": ["2"]
        }
        for column in df.columns:
            self.assertListEqual(df[column].tolist(), expected_data[column])

    def test_get_track_segments(self):
        segments = self.parser._get_track_segments(self.track_mock)
        self.assertEqual(segments, [self.track_segment_mock])

    def test_get_track_points(self):
        points = self.parser._get_track_points(self.track_segment_mock)
        self.assertEqual(points, [self.track_point_mock])

    def test_csv_row_structure_and_columns_length_match(self):
        result = self.parser._to_csv_row_structure(self.track_point_mock)
        self.assertEqual(len(result), len(self.parser.WORKOUT_ROUTE_COLUMNS))

class TestWorkoutRecordParser(unittest.TestCase):

    def setUp(self):
        # Setup mocks for XML elements
        self.workout_record_mock = MagicMock(spec=ET.Element)
        self.workout_route_mock = MagicMock(spec=ET.Element)
        self.metadata_entry_mock = MagicMock(spec=ET.Element)
        self.workout_statistics_mock = MagicMock(spec=ET.Element)

        # Configure mock responses
        self.workout_record_mock.get.side_effect = lambda x: {
            "workoutActivityType": "Running",
            "duration": "3600",
            "durationUnit": "s",
            "sourceName": "iPhone",
            "sourceVersion": "7.0",
            "device": "&lt;&lt;HKDevice: 0x1234d9876&gt;, name:iPhone, manufacturer:Apple Inc., model:iPhone, hardware:iPhone11,8, software:01.0&gt;",
            "creationDate": "2024-08-21T10:00:00Z",
            "startDate": "2024-08-21T09:00:00Z",
            "endDate": "2024-08-21T10:00:00Z"
        }.get(x)
        
        self.workout_route_mock.find.side_effect = lambda x: {
            "FileReference": MagicMock(attrib={"path": "path/to/file.gpx"})
        }.get(x)
        
        self.metadata_entry_mock.get.side_effect = lambda x: {
            "HKIndoorWorkout": "Outdoor",
            "HKWeatherTemperature": "25",
            "HKWeatherHumidity": "60",
            "HKTimeZone": "GMT",
            "HKAverageMETs": "8",
            "HKPhysicalEffortEstimationType": "1",
            "HKElevationAscended": "100",
            "HKElevationDescended": "50",
            "HKAverageSpeed": "12",
            "HKMaximumSpeed": "15",
            "HKSwimmingLocationType": "1",
            "HKSwimmingStrokeStyle": "2",
            "HKLapLength": "25",
            "HKSWOLFScore": "50",
            "HKWaterSalinity": "0"
        }.get(x)
        
        self.workout_statistics_mock.get.side_effect = lambda x: {
            "type": "HKQuantityTypeIdentifierActiveEnergyBurned",
            "sum": "500",
            "unit": "kcal"
        }.get(x)
        
        self.parser = WorkoutRecordParser(self.workout_record_mock)
        self.parser.workout_route = self.workout_route_mock
        self.parser.metadata_entries = [self.metadata_entry_mock]
        self.parser.workout_statistics = [self.workout_statistics_mock]

    def test_get_workout_record_data(self):
        result = self.parser._get_workout_record_data()
        expected = (
            "Running", "3600", "s", "iPhone", "7.0",
            "iPhone", "2024-08-21T10:00:00Z", 
            "2024-08-21T09:00:00Z", "2024-08-21T10:00:00Z"
        )
        self.assertEqual(result, expected)

    def test_csv_row_structure(self):
        result = self.parser.csv_row_structure()
        self.assertEqual(len(result), len(WorkoutRecordParser.MASTER_WORKOUT_COLUMNS))
        
    def test_columns_length_match(self):
        result = self.parser.csv_row_structure()
        self.assertEqual(len(result), len(WorkoutRecordParser.MASTER_WORKOUT_COLUMNS))


if __name__ == '__main__':
    unittest.main()
