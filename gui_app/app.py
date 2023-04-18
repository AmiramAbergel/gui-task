import logging
import threading

import webview
from flask import Flask

from gui_app import routes
from gui_app.utils import read_yaml, log_message


class GUIApp:

  def __init__(self,debug=False):
    self.app = self._initialize_app()
    self.app.secret_key = 'secret'
    self.debug = debug

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

  def _register_routes(self):
    routes.router(self.app, self)

  def _start_flask_app_thread(self):
    flask_app_thread = threading.Thread(target=self.app.run, kwargs={'host': '127.0.0.1', 'port': 5000})
    flask_app_thread.daemon = True
    flask_app_thread.start()

  def destroy(self):
    self.window.destroy()

  def _start_webview(self):
    self.window = webview.create_window('Frameless window', "http://127.0.0.1:5000", min_size=(800, 850),
                                        frameless=True)
    # by default, webview will start with debug=False
    webview.start(self.debug)

  @staticmethod
  def get_data():
    return read_yaml()


def main(debug=False):
  logging.basicConfig(
    filename='app.log',
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s',
  )
  log_message("Starting app.")
  gui_app = GUIApp(debug)
  gui_app.run()
  yaml_data = gui_app.get_data()
  return yaml_data
