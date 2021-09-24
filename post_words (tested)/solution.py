import json
from flask import Flask, request, jsonify

app = Flask(__name__)

words = []


@app.route('/', methods=["POST"])
def count_requests():
    word = request.json.get("word")
    words.append(word)
    response = words
    return jsonify(response)


if __name__ == '__main__':
    app.run()
