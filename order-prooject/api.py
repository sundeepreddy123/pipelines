import json

from flask import Flask, request

from order_lambda import lambda_handler as order_lambda


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():

    return {
        "message": "Order API is running"
    }


@app.route("/orders", methods=["POST"])
def create_order():

    request_body = request.get_json()

    event = {
        "body": json.dumps(request_body)
    }

    response = order_lambda(event, None)

    return response["body"], response["statusCode"], {
        "Content-Type": "application/json"
    }


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )