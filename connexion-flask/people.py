# people.py

from flask import make_response, abort, request, json
from config import db

from models import Person, people_schema, person_schema


def create():
    req_obj = request.get_data()
    if req_obj:
        body_data = json.loads(req_obj)
        lname = body_data.get("lname")
        fname = body_data.get("fname")
        existing_person = Person.query.filter(Person.lname == lname).one_or_none()
        if existing_person is None:
            new_person = person_schema.load({"lname": lname, "fname": fname}, session=db.session)
            db.session.add(new_person)
            db.session.commit()
            return person_schema.dump(new_person), 201
        else:
            abort(
                406,
                f"Person with last name {lname} already exists",
            )

def read_all():
    people = Person.query.all()
    return people_schema.dump(people)

def read_one(lname):
    person = Person.query.filter(Person.lname == lname).one_or_none()
    if person is not None:
        return person_schema.dump(person)
    else:
        abort(
            404, f"Person with last name {lname} not found"
        )
        
def update(lname):
    existing_person:Person = Person.query.filter(Person.lname == lname).one_or_none()
    if existing_person:
        req_obj = request.get_data()
        body_data = json.loads(req_obj)
        fname = body_data.get("fname")
        update_person = person_schema.load({"lname": lname, "fname": fname}, session=db.session)
        existing_person.fname = update_person.fname
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person), 201
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )
            
def delete(lname):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()
    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(
            f"{lname} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )