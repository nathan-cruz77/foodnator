from django.test.client import Client
from django.test.testcases import TestCase

from core.models import Cuisine

import json


class TestCuisine(TestCase):
    def test_list_cuisines(self):
        client = Client()

        r = client.get('/api/cuisines')
        self.assertEqual(200, r.status_code)

        cuisines = json.loads(r.content.decode('utf-8'))
        self.assertEqual(27, len(cuisines['data']))
