from collections import Counter

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, RadioField, SelectField, FileField, BooleanField, FieldList, FormField, PasswordField, \
  EmailField
from wtforms.validators import DataRequired, Email, ValidationError


def create_test_form(formdata=None, **kwargs):
  return TestForm(formData=formdata, **kwargs)


def create_user_form(formdata=None, **kwargs):
  return UserForm(formData=formdata, **kwargs)


def check_duplicate_emails(form, field):
  emails = [user_form.email.data for user_form in form.users.entries]
  email_counts = Counter(emails)

  duplicates = [email for email, count in email_counts.items() if count > 1]
  if duplicates:
    for user_form in form.users.entries:
      if user_form.email.data in duplicates:
        user_form.email.errors.append("Duplicate email detected")
        duplicates.remove(user_form.email.data)
    raise ValidationError("Duplicate email detected")


class PageForm(FlaskForm):
  def __init__(self, allowed_classes=None, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.allowed_classes = allowed_classes or []

    fields_to_remove = [field_name for field_name in self._fields if field_name not in self.allowed_classes]
    for field_name in fields_to_remove:
      if field_name == 'file_path':
        self._fields[field_name].data = ''
      else:
        del self._fields[field_name]

  mode = RadioField('Mode', name='mode', choices=[('debug', 'Debug'), ('production', 'Production')],
                    validators=[DataRequired()])
  tests = FieldList(FormField(create_test_form), name='tests', min_entries=10, max_entries=10,
                    validators=[DataRequired()])
  users = FieldList(FormField(create_user_form), name='users', min_entries=1, validators=[check_duplicate_emails])
  report_background_image = FileField('Report Background Image', id='file-input',
                                      validators=[
                                        FileAllowed(['jpeg', 'jpg', 'png'], 'Only JPG/JPEG/PNG files are allowed')],
                                      render_kw={'accept': '.png, .jpg, .jpeg'})
  file_path = StringField('File Path', id='file-path', validators=[], render_kw={"class": "form-control", "required": ""})
  hardware_acceleration = BooleanField('Hardware Acceleration')


class TestForm(FlaskForm):
  test_value = BooleanField(label='Test Checkbox')
  test_name = StringField(name='test_name')


class UserForm(FlaskForm):
  user_type = SelectField('Type', choices=[('admin', 'Admin'), ('standard', 'Standard')], validators=[DataRequired()])
  email = EmailField('Email', validators=[DataRequired(), Email(message='Invalid email address')])
  password = PasswordField('Password', validators=[DataRequired()])
