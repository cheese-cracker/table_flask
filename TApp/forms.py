from flask_wtf import FlaskForm
from wtforms import RadioField, FieldList, StringField
from wtforms.validators import DataRequired
from .jsonopener import file_list


class FileDetailForm(FlaskForm):
    file_ = RadioField('File Name*', choices=zip(file_list, file_list),
                       validators=[DataRequired()])
    fields = FieldList(StringField(), min_entries=6)
