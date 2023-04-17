import logging
import threading

import webview
from flask import Flask

import routes
from utils import read_yaml, log_message


class GUIApp:

  def __init__(self):
    self.app = self._initialize_app()
    self.app.secret_key = 'secret'

  @staticmethod
  def _initialize_app():
    app = Flask(__name__)
    app.config.update(
      WTF_CSRF_ENABLED=False,
      WTF_CSRF_CHECK_DEFAULT=False,
    )
    return app

  def run(self):
    self._register_routes()
    self._start_flask_app_thread()
    self._start_webview()
    self.app.run(debug=False)

  def _register_routes(self):
    routes.router(self.app, self)

  def _start_flask_app_thread(self):
    flask_app_thread = threading.Thread(target=self.app.run, kwargs={'host': '127.0.0.1', 'port': 5000})
    flask_app_thread.daemon = True
    flask_app_thread.start()
    self.flask_app_thread = flask_app_thread

  def destroy(self):
    self.window.destroy()

  def _start_webview(self):
    self.window = webview.create_window("My Flask App", "http://127.0.0.1:5000", min_size=(800, 600))
    # by default, webview will start with debug=False
    webview.start(debug=False)

  @staticmethod
  def get_data():
    yaml_data = read_yaml()
    return yaml_data


def main(callback=None):
  logging.basicConfig(
    filename='app.log',
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s',
  )
  log_message("Starting app.")
  gui_app = GUIApp()
  gui_app.run()
  if callback:
    yaml_data = gui_app.get_data()
    callback(yaml_data)


if __name__ == '__main__':
  main()
