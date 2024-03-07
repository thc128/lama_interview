from flask import Flask, request
from src.application_match_handler import application_match_handler


app = Flask(__name__)


@app.route("/applicationMatch", methods=["POST"])
def application_match():
    try:
        request_data = request.json
        result = application_match_handler(request_data)
        if result is None:
            return ["Unknown error"], 400
        return result, 200
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return ["An error occurred"], 500