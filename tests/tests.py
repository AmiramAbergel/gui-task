import unittest

import routes
from app import GUIApp


class TestGUIApp(unittest.TestCase):
    def setUp(self):
        self.gui_app = GUIApp()
        self.app = self.gui_app.app
        self.app.config['TESTING'] = True
        routes.router(self.app, self.gui_app)
        self.client = self.app.test_client()

    def test_page_one(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'App is running.', response.data)

    def test_page_two(self):
        response = self.client.get('/page-two')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Configuration saved.', response.data)

    def test_check_all(self):
        response = self.client.post('/check-all')
        self.assertEqual(response.status_code, 204)

        config_data = self.gui_app.get_data()
        for test in config_data['tests']:
            self.assertTrue(test['value'])

    def test_uncheck_all(self):
        response = self.client.post('/uncheck-all')
        self.assertEqual(response.status_code, 204)

        config_data = self.gui_app.get_data()
        for test in config_data['tests']:
            self.assertFalse(test['value'])

    def test_remove_row(self):
        initial_config_data = self.gui_app.get_data()
        initial_users_count = len(initial_config_data['users'])
        response = self.client.post('/remove-row/1')
        self.assertEqual(response.status_code, 204)

        updated_config_data = self.gui_app.get_data()
        updated_users_count = len(updated_config_data['users'])
        self.assertEqual(initial_users_count - 1, updated_users_count)

    def test_add_row(self):
        initial_config_data = self.gui_app.get_data()
        initial_users_count = len(initial_config_data['users'])
        response = self.client.post('/add-row/1')
        self.assertEqual(response.status_code, 204)

        updated_config_data = self.gui_app.get_data()
        updated_users_count = len(updated_config_data['users'])
        self.assertEqual(initial_users_count + 1, updated_users_count)

if __name__ == '__main__':
    unittest.main()