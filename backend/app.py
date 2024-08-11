from flask import Flask

FLASK_CONFIG = {
    "DEBUG": True,
}

app = Flask(__name__)
app.config.from_mapping(FLASK_CONFIG)


if __name__ == "__main__":
    app.run(debug=True)