"""Flask app for adopt app."""

from flask import Flask, render_template

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from flask_wtf import FlaskForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "abcdef"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.route("/")
def home_page():
    pets = Pet.query.all()
    return render_template("home-page.html", pets=pets)

