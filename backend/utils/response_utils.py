from flask import jsonify
from flask import Response


class UploadContextResponse:
    """
    A class to manage and generate responses related to file uploads.

    This class provides methods to build a response structure for file
    upload processes, including setting status codes, processing times,
    upload start and end times, and error messages. It ensures that the
    response structure is consistently formatted for the API responses.

    Typical usage example:

      response = UploadContextResponse()
      response.set_status_code(400)
      response.set_processing_time(123)
      response.add_error(1001, "Invalid file format.")
      return response.get_response()
    """
    def __init__(self):
        """Initializes the UploadContextResponse with default values.

        The default response structure includes a status code of 200, 
        processing time of 0, upload start and end times of 0, and 
        an empty list of errors.
        """
        self.response = {
            "uploadContext": {
                "statusCode": 200,
                "processingTime": 0,
                "uploadStartTime": 0,
                "uploadEndTime": 0,
                "errors": []
            }
        }

    def set_status_code(self, code: int):
        """Sets the status code in the response.

        Args:
            code (int): The HTTP status code to set.
        """
        self.response["uploadContext"]["statusCode"] = code

    def set_processing_time(self, processing_time: int):
        """Sets the processing time in seconds in the response.

        Args:
            processing_time (int): The time taken to process the file, in seconds.
        """
        self.response["uploadContext"]["processingTime"] = processing_time

    def set_upload_times(self, start_time: int, end_time: int):
        """Sets the upload start and end times in the response.

        Args:
            start_time (int): The timestamp when the upload started.
            end_time (int): The timestamp when the upload ended.
        """
        self.response["uploadContext"]["uploadStartTime"] = start_time
        self.response["uploadContext"]["uploadEndTime"] = end_time

    def add_error(self, error_code: int, error_message: int):
        """Sets the upload start and end times in the response.

        Args:
            start_time (int): The timestamp when the upload started.
            end_time (int): The timestamp when the upload ended.
        """
        error = {
            "errorCode": error_code,
            "errorMessage": error_message
        }
        self.response["uploadContext"]["errors"].append(error)

    def get_response(self) -> Response:
        """Generates the Flask response object.

        Returns:
            Response: The Flask response object with the JSON-encoded response data
                      and the appropriate HTTP status code.
        """
        return jsonify(self.response), self.response["uploadContext"]["statusCode"]

    def reset_errors(self):
        """Resets the errors list in the response to an empty list.
        """
        self.response["uploadContext"]["errors"] = []
