import os
import random

import yaml
from flask import request, flash
from werkzeug.utils import secure_filename
from yaml.loader import FullLoader

CONFIG_FILE = 'config.yaml'


def read_yaml():
  if not os.path.exists(CONFIG_FILE):
    return generate_random_config()
  else:
    with open(CONFIG_FILE, 'r') as yaml_file:
      try:
        data = yaml.load(yaml_file, Loader=FullLoader)
        return data
      except yaml.YAMLError as e:
        print(f"Error reading YAML file: {e}")
        return {}


def write_yaml(data):
  with open(CONFIG_FILE, 'w+') as yaml_file:
    try:
      yaml.dump(data, yaml_file)
    except yaml.YAMLError as e:
      print(f"Error writing YAML file: {e}")
      return {}


def generate_random_config():
  config_data = {
    'mode': 'debug',
    'tests': [
      {'name': 'Test 1', 'value': False},
      {'name': 'Test 2', 'value': False},
      {'name': 'Test 3', 'value': False},
      {'name': 'Test 4', 'value': False},
      {'name': 'Test 5', 'value': False},
      {'name': 'Test 6', 'value': False},
      {'name': 'Test 7', 'value': False},
      {'name': 'Test 8', 'value': False},
      {'name': 'Test 9', 'value': False},
      {'name': 'Test 10', 'value': False}
    ],
    'users': [
      {'user_type': 'Admin', 'email': '', 'password': ''},
      {'user_type': 'Standard', 'email': 'user@example.com', 'password': 'password'}
    ],
    'report_background_image': 'static/report_background.png',
    'hardware_acceleration': True
  }
  write_yaml(config_data)
  return config_data


def log_message(message):
  print(message)


def file_upload(f, form, app):
  filename = secure_filename(f.filename)
  f.save(os.path.join(
    app.static_folder, 'report_background_image', filename
  ))
  form_data = form.data
  file_path = os.path.join(
    app.static_folder, 'report_background_image', filename
  )
  form_data['report_background_image'] = {
    'filename': filename,
    'path': file_path
  }
  form_data['tests'] = [{'name': f'Test {i + 1}', 'value': bool(request.form.get(f"{form.tests.name}-{i}"))} for i
                        in range(len(form_data['tests']))]
  write_yaml(form_data)
  log_message("Saved configuration for Page.")
  flash('Configuration saved.')


def classesShuffle():
  classes = ['mode', 'tests', 'users', 'report', 'section']
  random.shuffle(classes)
  page_one_classes = classes[:3]
  page_two_classes = classes[3:]

  return page_one_classes, page_two_classes
