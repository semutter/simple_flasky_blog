# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired

class NewUser(Form):
    username = TextField("name", validators=[DataRequired()])
    email = TextField("email", validators=[DataRequired()]) #add support of email check

class NewPost(Form):
    title = TextField("title", validators=[DataRequired()])
    content = TextField("content", validators=[DataRequired()])
