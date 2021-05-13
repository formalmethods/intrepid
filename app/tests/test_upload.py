import intrepid
import unittest
from intrepid import PREFIX
import tempfile

CTX_NAME = 'default'

class UploadTestCase(unittest.TestCase):
    def setUp(self):
        self.app = intrepid.create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        intrepid.destroy_app()

    def test_upload_simple(self):
        NAME = 'upload.itd'
        f = tempfile.NamedTemporaryFile()
        f.write(
          b"""
          i1 = input bool
          n1 = not i1
          """
        )
        data = {'file': (open(f.name, 'rb'), NAME)}
        f.close()
        response = self.client.post(PREFIX + 'upload', data=data)
        self.assertEqual(201, response.status_code)
        self.assertEqual({
            'result': { 'ctx': '__ctx0' }}, response.get_json())
        response = self.client.get(PREFIX + 'inputs?context={}'.format('__ctx0'))
        self.assertEqual(200, response.status_code)
        self.assertEqual({'inputs': ['i1']}, response.get_json())

    def test_upload_error(self):
        NAME = 'upload.itd'
        f = tempfile.NamedTemporaryFile()
        f.write(
          b"""
          a = add b c
          """
        )
        data = {'file': (open(f.name, 'rb'), NAME)}
        f.close()
        response = self.client.post(PREFIX + 'upload', data=data)
        self.assertEqual(400, response.status_code)
        self.assertEqual({
            'result': 'Parse error at line 2: identifier b not found'
            }, response.get_json())

    def test_upload_and_add(self):
        NAME = 'upload.itd'
        f = tempfile.NamedTemporaryFile()
        f.write(
          b"""
          i1 = input bool
          i2 = input bool
          """
        )
        data = {'file': (open(f.name, 'rb'), NAME)}
        f.close()
        response = self.client.post(PREFIX + 'upload', data=data)
        self.assertEqual(201, response.status_code)
        self.assertEqual({
            'result': { 'ctx': '__ctx0' }}, response.get_json())
        response = self.client.post(PREFIX + 'nets/ands/create', \
                                    json={
                                      'context': '__ctx0',
                                      'x': 'i1',
                                      'y': 'i2'
                                    })
        self.assertEqual(201, response.status_code)

if __name__ == '__main__':
    unittest.main()
