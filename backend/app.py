from flask import Flask, request
from parsers.apple_health_export_parser import AppleHealthExportParser
from utils.file_utils import create_health_export_directories
from utils.response_utils import UploadResponse, RequestedWorkoutResponse, WorkoutDetailsResponse
import time

FLASK_CONFIG = {
    "DEBUG": True,
}

app = Flask(__name__)
app.config.from_mapping(FLASK_CONFIG)


@app.route("/api/export-status", methods=["GET"])
def send_data_status():
    return NotImplemented


@app.route("/api/upload", methods=["POST"])
def upload_export_file():
    response_builder = UploadResponse()
    upload_start_time = time.time()
    try:
        uploadedFile = request.files
        uploadedZip = uploadedFile['file']

        apple_health_export = AppleHealthExportParser(uploadedZip)
        apple_health_export.parse_health_elements()

        upload_end_time = time.time()

        response_builder.set_processing_time(
            upload_end_time - upload_start_time)
        response_builder.set_upload_times(upload_start_time, upload_end_time)

    except ValueError as ve:
        response_builder.set_status_code(400)
        response_builder.add_error(400, str(ve))
    except Exception as e:
        response_builder.set_status_code(500)
        response_builder.add_error(
            500, f"An unexpected error occurred: {str(e)}")

    return response_builder.get_response()


@app.route("/api/workout-details", methods=["GET"])
def send_all_workout_details():
    response_builder = WorkoutDetailsResponse()
    return response_builder.get_response()

@app.route("/api/workout", methods=["POST"])
def send_requested_workout():
    response_builder = RequestedWorkoutResponse()
    try:
        post_data = request.get_json()
        response_builder.generate_response(post_data['workoutStartDate'])
    except KeyError as ke:
        response_builder.set_status_code(500)
        response_builder.add_error(500, f"Internal Server Error: {str(ke)} is not a valid key.")
    except Exception as e:
        response_builder.set_status_code(500)
        response_builder.add_error(
            500, f"An unexpected error occurred: {str(e)}")

    return response_builder.get_response()


if __name__ == "__main__":
    create_health_export_directories()
    app.run(debug=True)
