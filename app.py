import webbrowser

from flask import Flask

import routes
from utils import read_yaml, log_message


class GUIApp:
  def __init__(self):
    self.app = Flask(__name__)
    self.app.secret_key = 'secret'

  def run(self):
    routes.router(self.app)
    url = "http://127.0.0.1:5000"
    webbrowser.open_new_tab(url)
    self.app.run(debug=True)

  def get_data(self):
    yaml_data = read_yaml()
    return yaml_data


if __name__ == '__main__':
  gui_app = GUIApp()
  gui_app.run()
  log_message("The script started.")
  yaml_data = gui_app.get_data()
  print(yaml_data)
