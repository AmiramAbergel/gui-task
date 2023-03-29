import os
import random

import yaml

CONFIG_FILE = 'config.yaml'


def read_yaml():
  if not os.path.exists(CONFIG_FILE):
    return generate_random_config()
  else:
    with open(CONFIG_FILE, 'r') as yaml_file:
      try:
        data = yaml.safe_load(yaml_file)
        return data
      except yaml.YAMLError as e:
        print(f"Error reading YAML file: {e}")
        return {}


def write_yaml(data):
  with open(CONFIG_FILE, 'w') as yaml_file:
    try:
      yaml.dump(data, yaml_file)
    except yaml.YAMLError as e:
      print(f"Error writing YAML file: {e}")
      return {}


def validate_email(email):
  return "@" in email and "." in email


def generate_random_config():
  config_data = {
    'mode': random.choice(['Debug', 'Production']),
    'tests': [f'Test {i}' for i in random.sample(range(1, 11), 5)],
    'users': [{'user_type': random.choice(['Admin', 'Standard']), 'email': 'test@test.com', 'password': 'password'} for
              i in range(1, 5)],
    'report_background_image': 'report_background.png',
    'hardware_acceleration': random.choice([True, False])
  }
  write_yaml(config_data)
  return config_data


def log_message(message):
  print(message)
