# models.py

# Marshmallow helps you to create a PersonSchema class, which is like the SQLAlchemy Person class you just created. 
# The PersonSchema class defines how the attributes of a class will be converted into JSON-friendly formats. 
# Marshmallow also makes sure that all attributes are present and contain the expected data type.

from datetime import datetime
from config import db, ma

class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), unique=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    
class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True # With load_instance, you’re able to deserialize JSON data and load Person model instances from it
        sqla_session = db.session

person_schema = PersonSchema()
people_schema = PersonSchema(many=True)