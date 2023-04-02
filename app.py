import webbrowser

from flask import Flask

import routes


class GUIApp:
  def __init__(self):
    self.app = Flask(__name__)
    self.app.secret_key = 'secret'

  def run(self):
    routes.router(self.app)
    url = "http://127.0.0.1:5000"
    webbrowser.open_new_tab(url)
    self.app.run(debug=True)


if __name__ == '__main__':
  gui_app = GUIApp()
  gui_app.run()
