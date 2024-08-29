from flask import jsonify
from flask import Response
from handlers import record_handler as record_handler
from handlers import workout_handler as workout_handler


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
            "workoutEventContext": {
                "totalWorkouts": 0,
                "distinctWorkouts": [],
                "workoutDateFreqMap": {}
            }
        }


class RequestedWorkoutResponse:
    def __init__(self, workout_start_date: str):
        self.workout_start_date = workout_start_date
        self.workout_csv = workout_handler.load_workout_csv()  # Works
        self.workout_data = workout_handler.get_workouts_from_date(
            self.workout_csv, self.workout_start_date)

        self.response = {
            "workoutContext": {
                "requestedDate": workout_start_date,
                "workouts": []
            },
        }

        self._build_response()

    def _build_response(self):
        for workout in self.workout_data:
            self.response["workoutContext"]["workouts"].append(
                {
                    "workoutName": workout["workoutActivityType"],
                    "workoutDuration": workout["duration"],
                    "workoutDurationUnit": workout["durationUnit"],
                    "workoutTotalDistance": workout["distanceWalkingRunning"],
                    "workoutTotalDistanceUnit": workout["distanceWalkingRunningUnit"],
                    "workoutTotalEnergyBurned": workout["activeEnergyBurned"],
                    "workoutTotalEnergyBurnedUnit": workout["activeEnergyBurnedUnit"],
                    "workoutCreationDate": workout["creationDate"],
                    "workoutStartDate": workout["startDate"],
                    "workoutEndDate": workout["endDate"],
                    "workoutStatistics": {
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
                            "chart": record_handler.load_record_into_chart_data("RunningGroundContactTime", workout["startDate"], workout["endDate"])
                        },
                        "runningPower": {
                            "average": workout['averageRunningPower'],
                            "minimum": workout['minimumRunningPower'],
                            "maximum": workout['maximumRunningPower'],
                            "unit": workout['runningPowerUnit'],
                            "chart": record_handler.load_record_into_chart_data("RunningPower", workout["startDate"], workout["endDate"])
                        },
                        "runningVerticalOscillation": {
                            "average": workout['averageRunningVerticalOscillation'],
                            "minimum": workout['minimumRunningVerticalOscillation'],
                            "maximum": workout['maximumRunningVerticalOscillation'],
                            "unit": workout['runningVerticalOscillationUnit'],
                            "chart": record_handler.load_record_into_chart_data("RunningVerticalOscillation", workout["startDate"], workout["endDate"])
                        },
                        "runningSpeed": {
                            "average": workout['averageRunningSpeed'],
                            "minimum": workout['minimumRunningSpeed'],
                            "maximum": workout['maximumRunningSpeed'],
                            "unit": workout['runningSpeedUnit'],
                            "chart": record_handler.load_record_into_chart_data("RunningSpeed", workout["startDate"], workout["endDate"])
                        },
                        "runningStrideLength": {
                            "average": workout['averageRunningStrideLength'],
                            "minimum": workout['minimumRunningStrideLength'],
                            "maximum": workout['maximumRunningStrideLength'],
                            "unit": workout['runningStrideLengthUnit'],
                            "chart": record_handler.load_record_into_chart_data("RunningStrideLength", workout["startDate"], workout["endDate"])
                        },
                        "distanceSwimming": {
                            "sum": workout['distanceSwimming'],
                            "unit": workout['distanceSwimmingUnit'],
                        },
                        "swimmingStrokeCount": {
                            "sum": workout['swimmingStrokeCount'],
                            "unit": workout['swimmingStrokeCountUnit'],
                        }
                    },
                    "workoutMetadata": {
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
                    },
                    "workoutRoute": {
                        'longitude': [],
                        'latitude': [],
                        'elevation': [],
                        'time': [],
                        'speed': [],
                        'course': [],
                        'hAcc': [],
                        'vAcc': []
                    },
                    "workoutVitals": {
                        "heartRate": {
                            "chart": record_handler.load_record_into_chart_data("HeartRate", workout["startDate"], workout["endDate"]),
                            "unit": workout['heartRateUnit']
                    }
                }
                }
            )





    def add_error(self, error_code: int, error_message: int):
        pass

    def get_response(self) -> Response:
        """Generates the Flask response object.

        Returns:
            Response: The Flask response object with the JSON-encoded response data
                      and the appropriate HTTP status code.
        """
        # return jsonify(self.response), 200
        return self.response
