"""
APIs for context
"""

import intrepid
import unittest
from intrepid import PREFIX

class ContextsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = intrepid.create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        intrepid.destroy_app()

    def test_root_not_found(self):
        response = self.client.get('/')
        self.assertEqual(404, response.status_code)

    def test_contexts(self):
        response = self.client.get(PREFIX + 'contexts')
        self.assertEqual(200, response.status_code)
        self.assertEqual({'contexts': []}, response.get_json())

    def test_create_context(self):
        NAME = 'banana'
        response = self.client.post(PREFIX + 'contexts/create', json={'name': NAME})
        self.assertEqual(201, response.status_code)
        self.assertEqual({'result': NAME}, response.get_json())
        response = self.client.get(PREFIX + 'contexts')
        self.assertEqual(200, response.status_code)
        self.assertEqual({'contexts': [NAME]}, response.get_json())

if __name__ == '__main__':
    unittest.main()
