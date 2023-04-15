import unittest

import routes
from app import GUIApp


class TestGUIApp(unittest.TestCase):
  def setUp(self):
    self.gui_app = GUIApp()
    self.app = self.gui_app.app
    self.app.config['TESTING'] = True
    routes.router(self.app)
    self.client = self.app.test_client()

  def test_page_one(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'App is running.', response.data)

  def test_next_button(self):
    response = self.client.post('/page-two')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Configuration saved.', response.data)

  def test_back_button(self):
    response = self.client.post('/')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'App is running.', response.data)

  def test_finish_button(self):
    pass

  def test_yaml_file(self):
    pass


if __name__ == '__main__':
  unittest.main()
