# -*- coding: utf-8 -*-

from blog import db
#from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    posts = db.relationship("Post", backref="user", lazy="dynamic")

    def __init__(self, username, email, register_time=None):
        self.username = username
        self.email = email

    def __repr__(self):
        return "<User %s>"%self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
