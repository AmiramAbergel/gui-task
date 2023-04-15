import logging
import webbrowser

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
        self._open_browser()
        self.app.run(debug=False)

    def _register_routes(self):
        routes.router(self.app)

    @staticmethod
    def _open_browser():
        url = "http://127.0.0.1:5000"
        webbrowser.open_new(url)

    def get_data(self):
        yaml_data = read_yaml()
        return yaml_data


def main():
    logging.basicConfig(
        filename='app.log',
        filemode='w',
        format='%(name)s - %(levelname)s - %(message)s',
    )
    log_message("Starting app.")
    gui_app = GUIApp()
    gui_app.run()
    yaml_data = gui_app.get_data()
    print(yaml_data)


if __name__ == '__main__':
    main()
