import unittest
from utils.response_utils import UploadResponse

class TestUploadResponse(unittest.TestCase):

    def setUp(self):
        """Set up the test case with a UploadResponse instance."""
        self.response = UploadResponse()

    def test_initialization(self):
        expected_response = {
            "uploadContext": {
                "statusCode": 200,
                "processingTime": 0,
                "uploadStartTime": 0,
                "uploadEndTime": 0,
                "errors": []
            }
        }
        self.assertEqual(self.response.response, expected_response)

    def test_set_status_code(self):
        self.response.set_status_code(404)
        self.assertEqual(self.response.response["uploadContext"]["statusCode"], 404)

    def test_set_processing_time(self):
        self.response.set_processing_time(120)
        self.assertEqual(self.response.response["uploadContext"]["processingTime"], 120)

    def test_set_upload_times(self):
        self.response.set_upload_times(1609459200, 1609462800)
        self.assertEqual(self.response.response["uploadContext"]["uploadStartTime"], 1609459200)
        self.assertEqual(self.response.response["uploadContext"]["uploadEndTime"], 1609462800)

    def test_add_error(self):
        self.response.add_error(4001, "Invalid file format.")
        expected_error = {
            "errorCode": 4001,
            "errorMessage": "Invalid file format."
        }
        self.assertIn(expected_error, self.response.response["uploadContext"]["errors"])

    def test_reset_errors(self):
        self.response.add_error(4001, "Invalid file format.")
        self.response.reset_errors()
        self.assertEqual(self.response.response["uploadContext"]["errors"], [])

if __name__ == '__main__':
    unittest.main()