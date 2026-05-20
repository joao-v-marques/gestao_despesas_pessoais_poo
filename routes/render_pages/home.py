from flask import Blueprint, render_template

bp_home = Blueprint("bp_home", __name__)

@bp_home.route("/home", methods=['GET'])
def render_home():
    return render_template("home.html")