import json

from django.test.client import Client
from django.test.testcases import TestCase

from core.tests import fixtures
from core.models import User


class TestSearchUsers(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.fake_users(3)
        fixtures.user_jon()

    def test_search_users(self):
        client = Client()
        user = User.objects.first()

        client.force_login(user)
        r = client.get('/api/users/search', { 'query': 'bla' })
        self.assertEqual(r.status_code, 200)

        suggestions = json.loads(r.content.decode('utf-8'))['data']
        self.assertEqual(len(suggestions), 3)
        self.assertNotIn('jon', suggestions)
