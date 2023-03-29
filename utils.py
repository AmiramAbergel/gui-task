import os
from functools import wraps

import yaml
from flask import flash


def read_yaml():
  if not os.path.exists('config.yaml'):
    return {}

  with open('config.yaml', 'r') as yaml_file:
    try:
      data = yaml.safe_load(yaml_file)
      return data
    except yaml.YAMLError as e:
      print(f"Error reading YAML file: {e}")
      return {}


def write_yaml(data):
  with open('config.yaml', 'w') as yaml_file:
    try:
      yaml.dump(data, yaml_file)
    except yaml.YAMLError as e:
      print(f"Error writing YAML file: {e}")
      return False
  return True


def validate_email(email):
  return "@" in email and "." in email


def flash_errors(form):
  for field, errors in form.errors.items():
    for error in errors:
      flash(f"{getattr(form, field).label.text}: {error}")


def validation_required(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    form = args[0]
    if not form.validate_on_submit():
      flash_errors(form)
      return False
    return func(*args, **kwargs)

  return wrapper
