from flask import jsonify

def validate_task(body):

    if not body:
        return None,(jsonify({"error": "json required"}), 400)

    if "title" not in body:
        return None, (jsonify({"error": "title required"}), 400)
    title=body["title"].strip()   

    if not body["title"].strip():
        return None, (jsonify({"error": "title cannot be empty"}), 400)
    
    return{
        "title":title
    }, None