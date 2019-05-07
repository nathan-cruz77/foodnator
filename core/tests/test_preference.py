from django.test.client import Client
from django.test.testcases import TestCase

from core.tests import fixtures
from core.models import Preference
from core.models import User
from core.models import Cuisine

import json


class TestPreference(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.fake_users()

    def test_update_preferences(self):
        client = Client()
        user = User.objects.get(username='bla0')
        client.force_login(user)

        r = client.post('/api/user/preferences', {
            'price': '1',
            'freeDelivery': 'false',
            'selectedCuisines': ['Brasileira'],
            'rejectedCuisines': ['Variada'],
            'rating': '0',
        })
        self.assertEqual(200, r.status_code)

        p = user.preference
        self.assertEqual(p.min_rating, 0)
        self.assertEqual(p.only_free_delivery, False)

        self.assertIn(Cuisine.objects.get(name='Brasileira'), p.selected_cuisines.all())
        self.assertIn(Cuisine.objects.get(name='Variada'), p.rejected_cuisines.all())

    def test_load_preference(self):
        client = Client()
        user = User.objects.get(username='bla0')
        client.force_login(user)
        client.post('/api/user/preferences', {
            'price': '1',
            'freeDelivery': 'false',
            'selectedCuisines': ['Brasileira'],
            'rejectedCuisines': ['Variada'],
            'rating': '0',
        })

        r = client.get('/api/user/preferences')
        self.assertEqual(200, r.status_code)

        data = json.loads(r.content.decode('utf-8'))
        self.assertEqual(1, data['price'])
        self.assertEqual(False, data['freeDelivery'])
        self.assertIn('Brasileira', data['selectedCuisines'])
        self.assertIn('Variada', data['rejectedCuisines'])
        self.assertEqual(0, data['rating'])
