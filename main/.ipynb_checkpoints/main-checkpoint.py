from flask import Flask, request, jsonify
from flask_cors import CORS

from app.agent import executor


app = Flask(__name__)

CORS(app)


@app.route("/question", methods=["POST"])
def chat():

    data = request.json

    user_message = data.get(
        "message"
    )


    if not user_message:
        return jsonify(
            {
                "error":
                "Message required"
            }
        )


    response = executor.invoke(
        {
            "input":
            user_message
        }
    )


    return jsonify(
        {
            "response":
            response["output"]
        }
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
