from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField, SubmitField, FileField, BooleanField, FieldList, FormField
from wtforms.validators import DataRequired, Email, Optional


def create_user_form(formdata=None, **kwargs):
  return UserForm(formdata=formdata, **kwargs)


class PageOneForm(FlaskForm):
  mode = RadioField('Mode', choices=[('debug', 'Debug'), ('production', 'Production')], validators=[DataRequired()])
  tests = FieldList(BooleanField('Test'), name='tests', min_entries=10, max_entries=10)
  users = FieldList(FormField(create_user_form), name='users', min_entries=1)
  report_background_image = FileField('Report Background Image', validators=[Optional()])
  next = SubmitField('Next')

class PageTwoForm(FlaskForm):
  hardware_acceleration = BooleanField('Hardware Acceleration')
  back = SubmitField('Back')
  finish = SubmitField('Finish')


class UserForm(FlaskForm):
  user_type = SelectField('Type', choices=[('admin', 'Admin'), ('standard', 'Standard')], validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = StringField('Password', validators=[DataRequired()])
