from setup_db import db
from marshmallow import Schema, fields


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)


class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    surname = fields.Str()
    password = fields.Str()
    email = fields.Str()
