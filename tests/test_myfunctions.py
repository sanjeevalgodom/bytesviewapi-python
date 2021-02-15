import os
from bytesviewapi import BytesviewApiClient  
import unittest 
import unittest

class test_bytesviwapi(unittest.TestCase):
    def setUp(self):
        # your private API key.
        key = os.environ.get("PYTEST_TOKEN")
        self.api = BytesviewApiClient(key)

    def test_name_gender_api(self):
        response = self.api.name_gender_api(data = {0: "ron"})
        self.assertEqual(str(list(response.keys())[0]), "0")
