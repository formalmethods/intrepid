import intrepid
import unittest
from intrepid import PREFIX

CTX_NAME = 'default'

class LatchesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = intrepid.create_app()
        self.client = self.app.test_client()
        response = self.client.post(PREFIX + 'contexts/create', json={'name': CTX_NAME})
        self.assertEqual(201, response.status_code)
        self.assertEqual({'result': CTX_NAME}, response.get_json())

    def tearDown(self):
        intrepid.destroy_app()

    def test_latches(self):
        response = self.client.get(PREFIX + 'latches?context={}'.format(CTX_NAME))
        self.assertEqual(200, response.status_code)
        self.assertEqual({'latches': []}, response.get_json())

    def test_create_latch(self):
        NAME = '__l0'
        response = self.client.post(PREFIX + 'latches/create', \
                                    json={
                                      'context': CTX_NAME,
                                      'type': 'bool'
                                    })
        self.assertEqual(201, response.status_code)
        self.assertEqual({'result': NAME}, response.get_json())
        response = self.client.get(PREFIX + 'latches?context={}'.format(CTX_NAME))
        self.assertEqual(200, response.status_code)
        self.assertEqual({'latches': [NAME]}, response.get_json())
        response = self.client.post(PREFIX + 'nets/true', \
                                    json={ 'context': CTX_NAME })
        self.assertEqual(201, response.status_code)
        self.assertEqual({'result': '__n1'}, response.get_json())
        response = self.client.put(PREFIX + 'latches/initnext', \
                                    json={
                                      'context': CTX_NAME,
                                      'latch': NAME,
                                      'init': '__n1',
                                      'next': '__n1'
                                    })
        self.assertEqual(200, response.status_code)
        self.assertEqual({'result': 'ok'}, response.get_json())

if __name__ == '__main__':
    unittest.main()
