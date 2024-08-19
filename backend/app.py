from flask import Flask, request, jsonify
from parsers.apple_health_export_parser import AppleHealthExportParser

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
    uploadedFile = request.files
    uploadedZip = uploadedFile['file']
    apple_health_export = AppleHealthExportParser(uploadedZip)
    apple_health_export.parse_health_elements()

    # TODO: Implement better response code
    return jsonify({}), 200

@app.route("/api/distinct-workouts", methods=["GET"])
def send_distinct_workouts():
    return NotImplementedError

@app.route("/api/workout", methods=["POST"])
def send_requested_workout():
    return NotImplementedError

if __name__ == "__main__":
    app.run(debug=True)
