"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash

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
    """Renders home page."""
    pets = Pet.query.all()
    return render_template("home-page.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet_form():
    """GET request renders the add pet form.
    POST request, if valid, creates a new instance of Pet, 
    commits is to database, and redirects the page."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, 
                  species=species, 
                  photo_url=photo_url, 
                  age=age, 
                  notes=notes)
        
        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name} the {species}")
        return redirect("/add")

    else:
        return render_template("add-pet-form.html", form=form)

@app.route("/<int:pet_id_number>", methods=["GET", "POST"])
def edit_pet_form(pet_id_number):
    """GET request renders the form with prepopulated
    values from the instance of Pet.
    POST request, if valid, sends values from form to 
    database and recommits the instance of Pet."""

    pet = Pet.query.get_or_404(pet_id_number)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, 
                  species=species, 
                  photo_url=photo_url, 
                  age=age, 
                  notes=notes)
        
        db.session.commit()
        
        flash(f"Updated {name}!")
        return redirect("/add")
     
    else:
        return render_template("add-pet-form.html", form=form)
