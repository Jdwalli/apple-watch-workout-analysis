from flask import jsonify
from flask import Response
from handlers import health_record_handler as health_record_handler
from handlers import workout_record_handler as workout_record_handler
import os 
import config
from utils import name_utils as name_utils


class UploadResponse:
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


class WorkoutDetailsResponse:
    def __init__(self):
        self.response = {
            "workoutDetailsContext": {
                "statusCode": 200,
                "totalWorkouts": 0,
                "workoutDates": [],
                "errors": []
            }
        }

    def _build_response(self):
        df = workout_record_handler.load_workout_records_into_dataframe()
        self.response["workoutDetailsContext"]["totalWorkouts"] = len(df)
        self.response["workoutDetailsContext"]["workoutDates"] = workout_record_handler.load_unique_workout_dates(
            df)
        
    def set_status_code(self, code: int):
        """Sets the status code in the response.

        Args:
            code (int): The HTTP status code to set.
        """
        self.response["workoutDetailsContext"]["statusCode"] = code


    def add_error(self, error_code: int, error_message: int):
        """Sets the upload start and end times in the response.

        Args:
        """
        error = {
            "errorCode": error_code,
            "errorMessage": error_message
        }
        self.response["workoutDetailsContext"]["errors"].append(error)

    def get_response(self) -> Response:
        """Generates the Flask response object.

        Returns:
            Response: The Flask response object with the JSON-encoded response data
                      and the appropriate HTTP status code.
        """
        self._build_response()
        return jsonify(self.response), self.response["workoutDetailsContext"]["statusCode"]


class RequestedWorkoutResponse:
    def __init__(self):
        self.workout_csv = None
        self.workout_data = None

        self.response = {
            "workoutContext": {
                "statusCode": 200,
                "requestedDate": "",
                "workouts": [],
                "errors": []
            },
        }

    def _build_response(self):
        for workout in self.workout_data:
            workout_stats = self._build_workout_stats(workout)
            self.response["workoutContext"]["workouts"].append(workout_stats)

    def _build_workout_stats(self, workout):
        return {
            "workoutName": name_utils.remove_workout_activity_type_prefix(workout["workoutActivityType"]),
            "workoutDeviceName": workout["sourceName"],
            "workoutDuration": workout["duration"],
            "workoutDurationUnit": workout["durationUnit"],
            "workoutTotalDistance": workout["distanceWalkingRunning"],
            "workoutTotalDistanceUnit": workout["distanceWalkingRunningUnit"],
            "workoutTotalEnergyBurned": workout["activeEnergyBurned"],
            "workoutTotalEnergyBurnedUnit": workout["activeEnergyBurnedUnit"],
            "workoutCreationDate": workout["creationDate"],
            "workoutStartDate": workout["startDate"],
            "workoutEndDate": workout["endDate"],
            "workoutStatistics": self._get_workout_statistics(workout),
            "workoutMetadata": self._get_workout_metadata(workout),
            "workoutRoute": workout_record_handler.load_workout_record_gpx_data(workout["FileReference"]),
            "workoutVitals": self._get_workout_vitals(workout),
        }

    def _get_workout_metadata(self, workout):
        return {
            "workoutLocationType": workout["indoorWorkout"],
            "averageMETs": workout["averageMETs"],
            "weatherTemperature": workout["temperature"],
            "weatherHumidity": workout["humidity"],
            "timeZone": workout["timeZone"],
            "maximumSpeed": workout['maximumSpeed'],
            "averageSpeed": workout['averageSpeed'],
            "physicalEffortEstimationType": workout["physicalEffortEstimationType"],
            "elevationAscended": workout['elevationAscended'],
            "elevationDescended": workout["elevationDescended"],
            "swimmingLocationType": workout["swimmingLocationType"],
            "swimmingStrokeStyle": workout["swimmingStrokeStyle"],
            "lapLength": workout['lapLength'],
            "swolfScore": workout['swolfScore'],
            "waterSalinity": workout['waterSalinity']
        }

    def _get_workout_vitals(self, workout):
        return {
            "heartRate": {
                "chart": health_record_handler.load_health_record_into_chart_format("HeartRate", workout["startDate"], workout["endDate"]),
                "unit": workout['heartRateUnit']
            }
        }

    def _get_workout_statistics(self, workout):
        return {
            "heartRate": {
                "average": workout["averageHeartRate"],
                "minimum": workout["minimumHeartRate"],
                "maximum": workout["maximumGroundContactTime"],
                "unit": workout["heartRateUnit"],
            },
            "activeEnergyBurned": {
                "sum": workout['activeEnergyBurned'],
                "unit": workout['activeEnergyBurnedUnit']
            },
            "basalEnergyBurned": {
                "sum": workout['basalEnergyBurned'],
                "unit": workout['basalEnergyBurnedUnit']
            },
            "distanceWalkingRunning": {
                "sum": workout['distanceWalkingRunning'],
                "unit": workout['distanceWalkingRunningUnit']
            },
            "stepCount": {
                "sum": workout['stepCount'],
                "unit": workout['stepCountUnit']
            },
            "runningGroundContactTime": {
                "average": workout["averageGroundContactTime"],
                "minimum": workout["minimumGroundContactTime"],
                "maximum": workout["maximumGroundContactTime"],
                "unit": workout["groundContactTimeUnit"],
                "chart": health_record_handler.load_health_record_into_chart_format("RunningGroundContactTime", workout["startDate"], workout["endDate"])
            },
            "runningPower": {
                "average": workout['averageRunningPower'],
                "minimum": workout['minimumRunningPower'],
                "maximum": workout['maximumRunningPower'],
                "unit": workout['runningPowerUnit'],
                "chart": health_record_handler.load_health_record_into_chart_format("RunningPower", workout["startDate"], workout["endDate"])
            },
            "runningVerticalOscillation": {
                "average": workout['averageRunningVerticalOscillation'],
                "minimum": workout['minimumRunningVerticalOscillation'],
                "maximum": workout['maximumRunningVerticalOscillation'],
                "unit": workout['runningVerticalOscillationUnit'],
                "chart": health_record_handler.load_health_record_into_chart_format("RunningVerticalOscillation", workout["startDate"], workout["endDate"])
            },
            "runningSpeed": {
                "average": workout['averageRunningSpeed'],
                "minimum": workout['minimumRunningSpeed'],
                "maximum": workout['maximumRunningSpeed'],
                "unit": workout['runningSpeedUnit'],
                "chart": health_record_handler.load_health_record_into_chart_format("RunningSpeed", workout["startDate"], workout["endDate"])
            },
            "runningStrideLength": {
                "average": workout['averageRunningStrideLength'],
                "minimum": workout['minimumRunningStrideLength'],
                "maximum": workout['maximumRunningStrideLength'],
                "unit": workout['runningStrideLengthUnit'],
                "chart": health_record_handler.load_health_record_into_chart_format("RunningStrideLength", workout["startDate"], workout["endDate"])
            },
            "distanceSwimming": {
                "sum": workout['distanceSwimming'],
                "unit": workout['distanceSwimmingUnit'],
            },
            "swimmingStrokeCount": {
                "sum": workout['swimmingStrokeCount'],
                "unit": workout['swimmingStrokeCountUnit'],
            }
        }

    def set_status_code(self, code: int):
        """Sets the status code in the response.

        Args:
            code (int): The HTTP status code to set.
        """
        self.response["workoutContext"]["statusCode"] = code

    def add_error(self, error_code: int, error_message: int):
        error = {
            "errorCode": error_code,
            "errorMessage": error_message
        }
        self.response["workoutContext"]["errors"].append(error)

    def generate_response(self, workout_start_date: str):
        self.response['workoutContext']['requestedDate'] = workout_start_date

        self.workout_csv = workout_record_handler.load_workout_records_into_dataframe()
        self.workout_data = workout_record_handler.load_workout_records_from_date(
            self.workout_csv, workout_start_date)

        self._build_response()

    def get_response(self) -> Response:
        """Generates the Flask response object.

        Returns:
            Response: The Flask response object with the JSON-encoded response data
                      and the appropriate HTTP status code.
        """

        return jsonify(self.response), self.response["workoutContext"]["statusCode"]

class ExportStatusResponse:
    def __init__(self):
        self.response = {
            "exportStatusContext": {
                "statusCode": 200,
                "exportPresent": False,
                "errors": []
            }
        }


    def _build_response(self):
        workout_file_path = os.path.join(
            config.WORKOUT_ELEMENTS_DIRECTORY, config.WORKOUTS_SUMMARY_FILE_NAME)
        self.response["exportStatusContext"]["exportPresent"] = os.path.isfile(workout_file_path)
    
    def set_status_code(self, code: int):
        """Sets the status code in the response.

        Args:
            code (int): The HTTP status code to set.
        """
        self.response["exportStatusContext"]["statusCode"] = code


    def add_error(self, error_code: int, error_message: int):
        """Sets the upload start and end times in the response.

        Args:
        """
        error = {
            "errorCode": error_code,
            "errorMessage": error_message
        }
        self.response["exportStatusContext"]["errors"].append(error)

    def get_response(self) -> Response:
        """Generates the Flask response object.

        Returns:
            Response: The Flask response object with the JSON-encoded response data
                      and the appropriate HTTP status code.
        """
        self._build_response()
        return jsonify(self.response), self.response["exportStatusContext"]["statusCode"]
    