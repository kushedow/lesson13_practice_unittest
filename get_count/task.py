import json
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    1: {"name": "Alice", "age": 16, "location": "Moscow"},
    2: {"name": "Boris", "age": 14, "location": "Moscow"},
    3: {"name": "Margo", "age": 20, "location": "Irkutsk"},
    4: {"name": "Denis", "age": 27, "location": "Ufa"},
}


@app.route('/count-users/')
def count_users():
    response = {"count": len(users)}
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(port=5010)
