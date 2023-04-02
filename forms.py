from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, RadioField, SelectField, SubmitField, FileField, BooleanField, FieldList, FormField
from wtforms.validators import DataRequired, Email


def create_user_form(formData=None, **kwargs):
  return UserForm(formData=formData, **kwargs)


class TestForm(FlaskForm):
  name = StringField('Name')
  value = BooleanField('Value')


def generate_default_tests():
  tests = [{'name': f'Test {i}', 'value': False} for i in range(1, 11)]
  return tests


class PageOneForm(FlaskForm):
  mode = RadioField('Mode', name='mode', choices=[('debug', 'Debug'), ('production', 'Production')],
                    validators=[DataRequired()])
  tests = FieldList(FormField(TestForm, default=generate_default_tests), name='tests', min_entries=10, max_entries=10,
                    validators=[DataRequired()])
  users = FieldList(FormField(create_user_form), name='users', min_entries=1)
  report_background_image = FileField('Report Background Image',
                                      validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
  hardware_acceleration = BooleanField('Hardware Acceleration')
  next = SubmitField('Next')


class UserForm(FlaskForm):
  user_type = SelectField('Type', choices=[('admin', 'Admin'), ('standard', 'Standard')], validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = StringField('Password', validators=[DataRequired()])
