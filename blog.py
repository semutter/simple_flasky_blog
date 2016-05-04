#!/usr/bin/env python
# -*- coding: utf-8 -*

from flask import Flask, request, render_template, url_for, redirect, flash
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + "/home/fenghan/flask_blog/raw_data.db"
app.config["SECRET_KEY"] = 'a random string'

db = SQLAlchemy(app)
from models import *
from html_forms import NewUser

@app.route("/")
def index():
    return redirect(url_for("all_user_list"))

@app.route("/hello")
def hello_world():
    return "Hello World!"


@app.route("/blog", methods=["post", "get"])
def all_user_list():
    new_user_form = NewUser(request.form)
    if request.method == "GET":
        user_list = User.query.all()
        return render_template("user_list.html", user_list=user_list, form=new_user_form)
    if request.method == "POST" and new_user_form.validate():
        user = User(new_user_form.username.data, new_user_form.email.data)
        db.session.add(user)
        db.session.commit()
        flash("Successfully add a new user!")
        return redirect(url_for("all_user_list"))
    return redirect(url_for("error"))

@app.route("/user/<int:user_id>")
def user_blog_list(user_id):
    user_blog_list = Post.query.filter_by(user_id=user_id).all()
    user = User.query.filter_by(id=user_id).first()
    return render_template("blog_list.html", user=user, blog_list=user_blog_list)

@app.route("user/<int:user_id>/add_blog", methods=["GET", "POST"])
def user_add_blog():
    pass

@app.route("/error")
def error():
    return "ERROR Page!"








if __name__ == "__main__":
    app.run(debug=True)
