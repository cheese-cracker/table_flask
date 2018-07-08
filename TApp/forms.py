from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList
from wtforms.validators import DataRequired


class FileDetailForm(FlaskForm):
    file_ = StringField('File Name*', validators=[DataRequired()])
    fields = FieldList(StringField(), min_entries=6)
    submit = SubmitField('TABULATE')
