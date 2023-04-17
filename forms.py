from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, RadioField, SelectField, FileField, BooleanField, FieldList, FormField, PasswordField, \
  EmailField
from wtforms.validators import DataRequired, Email


def create_test_form(formdata=None, **kwargs):
  return TestForm(formData=formdata, **kwargs)


def create_user_form(formdata=None, **kwargs):
  return UserForm(formData=formdata, **kwargs)


class PageForm(FlaskForm):
  def __init__(self, allowed_classes=None, *args, **kwargs):
    super(PageForm, self).__init__(*args, **kwargs)
    self.allowed_classes = allowed_classes or []

    fields_to_remove = [field_name for field_name in self._fields if field_name not in self.allowed_classes]
    for field_name in fields_to_remove:
      del self._fields[field_name]

  mode = RadioField('Mode', name='mode', choices=[('debug', 'Debug'), ('production', 'Production')],
                    validators=[DataRequired()])
  tests = FieldList(FormField(create_test_form), name='tests', min_entries=10, max_entries=10,
                    validators=[DataRequired()])
  users = FieldList(FormField(create_user_form), name='users', min_entries=1)
  report_background_image = FileField('Report Background Image', id='file-input',
                                      validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Only "jpg" and "png" files are allowed')])
  file_path = StringField('File Path', id='file-path', validators=[])
  hardware_acceleration = BooleanField('Hardware Acceleration')


class TestForm(FlaskForm):
  test_value = BooleanField(label='Test Checkbox')
  test_name = StringField(name='test_name')


class UserForm(FlaskForm):
  user_type = SelectField('Type', choices=[('admin', 'Admin'), ('standard', 'Standard')], validators=[DataRequired()])
  email = EmailField('Email', validators=[DataRequired(), Email(message='Invalid email address')]) #, render_kw={'pattern':'.+@globex\.com'}
  password = PasswordField('Password', validators=[DataRequired()])
