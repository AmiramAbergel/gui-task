import os
import random

import yaml
from flask import url_for, redirect, request
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
        log_message("Error reading YAML file.")
        print(f"Error reading YAML file: {e}")

        return {}


def write_yaml(data):
  if not os.path.exists(CONFIG_FILE):
    existing_data = {}
  else:
    existing_data = read_yaml()
  existing_data.update(data)
  with open(CONFIG_FILE, 'w') as yaml_file:
    try:
      yaml.safe_dump(existing_data, yaml_file)
    except yaml.YAMLError as e:
      log_message("Error writing YAML file.")
      print(f"Error writing YAML file: {e}")


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
      {'user_type': 'admin', 'email': '', 'password': ''}
    ],
    'hardware_acceleration': True
  }
  write_yaml(config_data)

  return config_data


def log_message(message):
  print(message)


def file_upload(file, form, app, config_data, route_name):
  if file:
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.static_folder, 'report_background_image', filename)
    file.save(file_path)
    form.report_background_image.data = {'filename': filename, 'path': file_path}
  updated_form = tests_convert_to_dict(form.data)
  write_yaml(updated_form)
  log_message("Saved configuration for Page.")

  return redirect(url_for(route_name))


def tests_convert_to_dict(form_data):
  tests_data = form_data.get('tests', [])
  if len(tests_data) == 0:
    return form_data
  tests_list = [{'name': f"Test {index + 1}", 'value': item['test_value']} for index, item in enumerate(tests_data)]
  form_data['tests'] = tests_list

  return form_data


def classes_shuffle():
  classes = ['mode', 'tests', 'users', 'report_background_image', 'hardware_acceleration']
  random.shuffle(classes)
  page_one_classes = classes[:3]
  page_two_classes = classes[3:]

  return page_one_classes, page_two_classes


def process_form(form, app, config_data, route_name):
  form.process(request.form)
  file = request.files.get('report_background_image')
  if file:
    return file_upload(file, form, app, config_data, route_name)
  else:
    updated_form = tests_convert_to_dict(form.data)
    write_yaml(updated_form)
    return redirect(url_for(route_name))


def shutdown_server(gui_app):
  func = request.environ.get('werkzeug.server.shutdown')
  if func is None:
    raise RuntimeError('Not running with the Werkzeug Server')
  func()
  gui_app.destroy()
  return