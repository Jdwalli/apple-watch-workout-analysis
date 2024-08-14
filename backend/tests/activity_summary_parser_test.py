import unittest
from unittest.mock import Mock
import xml.etree.ElementTree as ET
from parsers import activity_summary_parser
from config import HeartRateMotionContext


class TestActivitySummaryParser(unittest.TestCase):

    def setUp(self):
        self.mock_record_element = Mock(spec=ET.Element)
        self.mock_record_element.tag = 'ActivitySummary'
        self.mock_record_element.get.side_effect = lambda key: {
            "dateComponents": '1983-01-01',
            "activeEnergyBurned": '123',
            "activeEnergyBurnedGoal": '124',
            "activeEnergyBurnedUnit": 'cal',
            "appleMoveTime": '50',
            "appleMoveTimeGoal": '45',
            "appleExerciseTime": '60',
            "appleExerciseTimeGoal": '60',
            "appleStandHours": '2',
            "appleStandHoursGoal": '9'
        }.get(key, None)


    def test_activity_summary_parser_rejects_wrong_tag(self):
        self.mock_record_element.tag = "NotActivitySummary"
        with self.assertRaises(TypeError):
            activity_summary_parser.ActivitySummaryParser(
            self.mock_record_element)

    def test_csv_row_structure(self):
        parser = activity_summary_parser.ActivitySummaryParser(
            self.mock_record_element)
        result = parser.csv_row_structure()

        expected = (
            "1983-01-01",
            "123",
            "124",
            "cal",
            "50",
            "45",
            "60",
            "60",
            "2",
            "9"
        )
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
