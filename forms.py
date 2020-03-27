"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField("Pet name",
                       validators=[InputRequired()])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
                          validators=[InputRequired()])
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    age = SelectField("Age", choices=[("baby", "Baby"), ("young", "Young"), ("adult", "Adult"), ("senior", "Senior")])
    notes = StringField("Notes")
