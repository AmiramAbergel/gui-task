from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, RadioField, SelectField, FileField, BooleanField, FieldList, FormField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError

from utils import log_message


def create_test_form(formData=None, **kwargs):
  return TestForm(formData=formData, **kwargs)


def create_user_form(formData=None, **kwargs):
  return UserForm(formData=formData, **kwargs)


def validate_users(field):
  for user_entry in field.entries:
    if not (user_entry.user_type.data and user_entry.email.data and user_entry.password.data):
      log_message("You can't add a line if any cells in it are still empty.")
      raise ValidationError("You can't add a line if any cells in it are still empty.")


class PageForm(FlaskForm):
  def __init__(self, allowed_classes=None, *args, **kwargs):
    super(PageForm, self).__init__(*args, **kwargs)
    self.allowed_classes = allowed_classes or []

    fields_to_remove = []
    for field_name, field_obj in self._fields.items():
      if field_name not in self.allowed_classes:
        fields_to_remove.append(field_name)

    for field_name in fields_to_remove:
      del self._fields[field_name]

  mode = RadioField('Mode', name='mode', choices=[('debug', 'Debug'), ('production', 'Production')],
                    validators=[DataRequired()])
  tests = FieldList(FormField(create_test_form), name='tests', min_entries=10, max_entries=10,
                    validators=[DataRequired()])
  users = FieldList(FormField(create_user_form), name='users', min_entries=1, validators=[validate_users])
  report_background_image = FileField('Report Background Image',
                                      validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
  hardware_acceleration = BooleanField('Hardware Acceleration')


class TestForm(FlaskForm):
  test_value = BooleanField('Test Value')


class UserForm(FlaskForm):
  user_type = SelectField('Type', choices=[('admin', 'Admin'), ('standard', 'Standard')], validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
