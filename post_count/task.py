import json
from flask import Flask, request, jsonify

app = Flask(__name__)

requested = []


@app.route('/count/')
def count_requests():
    requested.append("")
    response = {"count": len(requested)}
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=5002)
