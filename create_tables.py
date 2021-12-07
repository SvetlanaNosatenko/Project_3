import os

from dao.model.user import User
from app import create_app
from setup_db import db

app = create_app()

with app.app_context():
    db.create_all()