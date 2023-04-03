from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, RadioField, SelectField, SubmitField, FileField, BooleanField, FieldList, FormField, \
  PasswordField
from wtforms.validators import DataRequired, Email, ValidationError


def create_user_form(formData=None, **kwargs):
  return UserForm(formData=formData, **kwargs)


def validate_users(field):
  for user_entry in field.entries:
    if not (user_entry.user_type.data and user_entry.email.data and user_entry.password.data):
      raise ValidationError("You can't add a line if any cells in it are still empty.")


class TestForm(FlaskForm):
  name = StringField('Name')
  value = BooleanField('Value')


class PageOneForm(FlaskForm):
  mode = RadioField('Mode', name='mode', choices=[('debug', 'Debug'), ('production', 'Production')],
                    validators=[DataRequired()])
  tests = FieldList(FormField(TestForm), name='tests', min_entries=10, max_entries=10,
                    validators=[DataRequired()])
  users = FieldList(FormField(create_user_form), name='users', min_entries=1, validators=[validate_users])
  report_background_image = FileField('Report Background Image',
                                      validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
  hardware_acceleration = BooleanField('Hardware Acceleration')
  next = SubmitField('Next')


class UserForm(FlaskForm):
  user_type = SelectField('Type', choices=[('admin', 'Admin'), ('standard', 'Standard')], validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
