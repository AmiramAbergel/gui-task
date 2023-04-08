import logging
import webbrowser

from flask import Flask

import routes
from utils import read_yaml, log_message


class GUIApp:

  def __init__(self):
    self.app = Flask(__name__)
    self.app.secret_key = 'secret'
    self.app.config.update(WTF_CSRF_ENABLED=False)
    self.app.config.update(WTF_CSRF_CHECK_DEFAULT=False)



  def run(self):
    routes.router(self.app)
    url = "http://127.0.0.1:5000"
    webbrowser.open_new(url)
    self.app.run(debug=False)

  def get_data(self):
    yaml_data = read_yaml()
    return yaml_data


if __name__ == '__main__':
  logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
  log_message("Starting app.")
  gui_app = GUIApp()
  gui_app.run()
  yaml_data = gui_app.get_data()
  print(yaml_data)
