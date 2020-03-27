"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField


class AddPetForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField("Pet name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = SelectField("Age",
                      choices=[("baby", "Baby"), 
                               ("young", "Young"), 
                               ("adult", "Adult"), 
                               ("senior", "Senior")])
    notes = StringField("Notes")
