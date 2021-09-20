from forms.login import LoginForm
from flask import Blueprint, render_template, request, redirect
from flask.helpers import flash, url_for
from flask.json import jsonify
from flask_wtf import form

views = Blueprint(__name__, "views")

@views.route("/test")
def test():
    return "Login Success!"

## Return HTML content
@views.route("/home", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for("views.test"))
    return render_template("login.html", title="Login", form=form)


## Return HTML content
@views.route("/index")
def index():
    return render_template("index.html", name="Suhas", company="SAAL", title="Suhas Learns Python")

## Read Query Parameter
@views.route("/profile/<username>")
def profile(username):
    return render_template("profile.html", name=username)

## Read URL Query Param
@views.route("/profile")
def profile1():
    args = request.args
    username = args.get('name')
    return render_template("profile.html", name=username)

## Return JSON beautified
@views.route('/json')
def get_json():
    return jsonify({'name':'suhas', 'age':10, 'country':'Abu Dhabi, UAE'})

## Accept JSON input
@views.route("/data")
def post_data():
    data = request.json
    return jsonify(data)

## Redirect
@views.route('go-to-home')
def go_to_home():
    return redirect(url_for("views.home"))

## Template Inheritence
@views.route("/testblock")
def testblock():
    return render_template("home.html")