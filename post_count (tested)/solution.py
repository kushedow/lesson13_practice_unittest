import json
from flask import Flask, request, jsonify

app = Flask(__name__)

status = {"count": 0}  # используйте этот словарь, он используется для проверки


@app.route('/count/', methods=["POST"])
def count_requests():
    status["count"] += 1
    return jsonify(status)


if __name__ == '__main__':
    app.run()
