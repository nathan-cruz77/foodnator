from django.test.client import Client
from django.test.testcases import TestCase

from core.tests import fixtures
from core.models import Group
from core.models import User

import json


class TestGroup(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.fake_groups()

    def test_list_groups(self):
        client = Client()
        client.force_login(User.objects.get(username='bla0'))

        r = client.get('/api/groups')
        self.assertEqual(200, r.status_code)

        groups = [g['name'] for g in json.loads(r.content.decode('utf-8'))['data']]
        self.assertEqual(['Grupão doido', 'Só no back-end'], groups)
