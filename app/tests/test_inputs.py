"""
Copyright (C) 2021 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 08/02/2021
"""
import intrepid
import unittest
from intrepid import PREFIX

CTX_NAME = 'default'

class InputsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = intrepid.create_app()
        self.client = self.app.test_client()
        response = self.client.post(PREFIX + 'contexts/create', json={'name': CTX_NAME})
        self.assertEqual(201, response.status_code)
        self.assertEqual({'result': CTX_NAME}, response.get_json())

    def tearDown(self):
        intrepid.destroy_app()

    def test_inputs(self):
        response = self.client.get(PREFIX + 'inputs?context={}'.format(CTX_NAME))
        self.assertEqual(200, response.status_code)
        self.assertEqual({'inputs': []}, response.get_json())

    def test_create_input(self):
        NAME = '__i0'
        response = self.client.post(PREFIX + 'inputs/create', \
                                    json={
                                      'context': CTX_NAME,
                                      'type': 'bool'
                                    })
        self.assertEqual(201, response.status_code)
        self.assertEqual({'result': NAME}, response.get_json())
        response = self.client.get(PREFIX + 'inputs?context={}'.format(CTX_NAME))
        self.assertEqual(200, response.status_code)
        self.assertEqual({'inputs': [NAME]}, response.get_json())

    def test_create_inputs(self):
        response = self.client.post(PREFIX + 'inputs/create', \
                                    json={
                                      'context': CTX_NAME,
                                      'type': 'bool'
                                    })
        self.assertEqual(201, response.status_code)
        self.assertEqual({'result': '__i0'}, response.get_json())
        response = self.client.post(PREFIX + 'inputs/create', \
                                    json={
                                      'context': CTX_NAME,
                                      'type': 'bool'
                                    })
        self.assertEqual(201, response.status_code)
        self.assertEqual({'result': '__i1'}, response.get_json())
        response = self.client.get(PREFIX + 'inputs?context={}'.format(CTX_NAME))
        self.assertEqual(200, response.status_code)
        self.assertEqual({'inputs': ['__i0', '__i1']}, response.get_json())

if __name__ == '__main__':
    unittest.main()
