import os
import random

import yaml
from flask import flash, url_for, redirect
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
  if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'r') as yaml_file:
      try:
        existing_data = yaml.safe_load(yaml_file)
        if existing_data is None:
          existing_data = {}
      except yaml.YAMLError as e:
        print(f"Error reading YAML file: {e}")
        return {}
  else:
    existing_data = {}

  existing_data.update(data)

  with open(CONFIG_FILE, 'w') as yaml_file:
    try:
      yaml.safe_dump(existing_data, yaml_file)
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


def file_upload(file, form, app, route_name):
  filename = secure_filename(file.filename)
  file.save(os.path.join(app.static_folder, 'report_background_image', filename))
  file_path = os.path.join(
    app.static_folder, 'report_background_image', filename
  )
  if file:
    form.report_background_image.data = file_path
    config_data = read_yaml()
    config_data['report_background_image'] = {
      'filename': filename,
      'path': file_path
    }

    write_yaml(config_data)
    flash('Configuration saved.')
    log_message("Saved configuration for Page.")
  else:
    write_yaml(form.data)

  return redirect(url_for(route_name))


def classesShuffle():
  classes = ['mode', 'tests', 'users', 'report_background_image', 'hardware_acceleration']
  random.shuffle(classes)
  page_one_classes = classes[:3]
  page_two_classes = classes[3:]

  return page_one_classes, page_two_classes
