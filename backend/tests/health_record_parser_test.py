import unittest
from unittest.mock import Mock
import xml.etree.ElementTree as ET
from parsers import health_record_parser
from config import HeartRateMotionContext


class TestHealthRecordParser(unittest.TestCase):

    def setUp(self):
        self.mock_record_element_type = "HKQuantityTypeIdentifierHeartRate"
        self.mock_record_element = Mock(spec=ET.Element)
        self.mock_record_element.tag = 'Record'
        self.mock_record_element.get.side_effect = lambda key: {
            "type": self.mock_record_element_type,
            "sourceName": "Mock Test Source",
            "sourceVersion": "1.0.0",
            "device": "Unknown",
            "unit": "wpm",
            "creationDate": "123",
            "startDate": "456",
            "endDate": "789",
            "value": "123"
        }.get(key, None)

        self.metadata_entries = [
            Mock(spec=ET.Element, tag='MetadataEntry', get=lambda key: {
                'key': 'HKMetadataKeyHeartRateMotionContext',
                'value': '1'
            }.get(key, None)),
        ]
        self.mock_record_element.findall.return_value = self.metadata_entries

    def test_csv_row_structure_with_heart_rate_record_type(self):
        parser = health_record_parser.HealthRecordParser(
            self.mock_record_element)
        result = parser.csv_row_structure()

        expected = (
            "HeartRate",
            "wpm",
            "123",
            "Mock Test Source",
            "1.0.0",
            "Unknown",
            "123",
            "456",
            "789",
            HeartRateMotionContext.SEDENTARY.name
        )
        self.assertEqual(result, expected)

    def test_csv_row_structure_with_heart_rate_record_type_and_columns_length_match(self):
        parser = health_record_parser.HealthRecordParser(
            self.mock_record_element)
        result = parser.csv_row_structure()

        self.assertEqual(len(result), len(parser.HEART_RATE_RECORD_COLUMNS))

    def test_csv_row_structure_with_record_without_metadata(self):
        self.mock_record_element_type = "HKQuantityTypeIdentifierStepCount"

        parser = health_record_parser.HealthRecordParser(
            self.mock_record_element)
        result = parser.csv_row_structure()

        expected = (
            "StepCount",
            "wpm",
            "123",
            "Mock Test Source",
            "1.0.0",
            "Unknown",
            "123",
            "456",
            "789"
        )
        self.assertEqual(result, expected)

    def test_csv_row_structure_with_record_without_metadata_and_columns_length_match(self):
        self.mock_record_element_type = "HKQuantityTypeIdentifierStepCount"
        parser = health_record_parser.HealthRecordParser(
            self.mock_record_element)
        result = parser.csv_row_structure()

        self.assertEqual(len(result), len(parser.DEFAULT_HEALTH_RECORD_COLUMNS))


if __name__ == '__main__':
    unittest.main()
