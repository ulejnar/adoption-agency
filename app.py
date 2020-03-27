"""Flask app for adopt app."""

from flask import Flask, render_template, redirect

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from flask_wtf import FlaskForm
from forms import AddPetForm

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

@app.route("/add", methods=["GET", "POST"])
def add_pet_form():

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        # if age is in this range, young, elif

        pet = Pet(name=name, 
                  species=species, 
                  photo_url=photo_url, 
                  age=age, 
                  notes=notes)
        
        db.session.add(pet)
        db.session.commit()

        return redirect("/add")

    else:
        return render_template("add-pet-form.html", form=form)