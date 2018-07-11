from flask_wtf import FlaskForm
from wtforms import StringField, FieldList
from wtforms.validators import DataRequired


class FileDetailForm(FlaskForm):
    file_ = StringField('File Name*', validators=[DataRequired()])
    fields = FieldList(StringField(), min_entries=6)
