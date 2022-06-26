from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import nullslast

db = SQLAlchemy()


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)
    # posts=


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    # categories=db.
    # tags=db.


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    __password = db.Column(db.String, nullable=False)
    # posts= db


def configure(app: Flask):
    with app.app_context():
        db.init_app(app)
        db.create_all()
