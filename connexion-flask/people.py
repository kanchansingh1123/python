# people.py

from datetime import datetime

from flask import abort, jsonify, request, json

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

PEOPLE = {
    "Fairy": {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": get_timestamp(),
    },
    "Ruprecht": {
        "fname": "Knecht",
        "lname": "Ruprecht",
        "timestamp": get_timestamp(),
    },
    "Bunny": {
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": get_timestamp(),
    }
}

def create():
    req_obj = request.get_data()
    if req_obj:
        body_data = json.loads(req_obj)
        lname = body_data.get("lname")
        fname = body_data.get("fname")
        if lname and lname not in PEOPLE:
            PEOPLE[lname] = {
                "lname": lname,
                "fname": fname,
                "timestamp": get_timestamp(),
            }
            return PEOPLE[lname], 201
        else:
            abort(
                406,
                f"Person with last name {lname} already exists",
            )

def read_all():
    return list(PEOPLE.values())

def read_one(lname):
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(
            404, f"Person with last name {lname} not found"
        )