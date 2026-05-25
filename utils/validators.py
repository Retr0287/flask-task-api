from flask import jsonify

def validate_task(body):

    if not body:
        return jsonify({"error": "json required"}), 400

    if "title" not in body:
        return jsonify({"error": "title required"}), 400

    if not body["title"].strip():
        return jsonify({"error": "title cannot be empty"}), 400