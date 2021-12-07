from setup_db import db
from marshmallow import Schema, fields


class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))


class FavoriteSchema(Schema):
    id = fields.Int()
    user_id = fields.Str()
    movie_id = fields.Str()

