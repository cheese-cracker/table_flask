from flask_wtf import FlaskForm
from wtforms import RadioField, FieldList, StringField
from wtforms.validators import DataRequired
from .jsonopener import get_flst


class FileDetailForm(FlaskForm):
    file_ = RadioField('File Name*',
                       choices=zip(get_flst(), get_flst()))
                       # validators=[DataRequired()])
    fields = FieldList(StringField(), min_entries=6)
