from django.test.client import Client
from django.test.testcases import TestCase

from core.tests import fixtures
from core.models import Group
from core.models import User
from core.models import Restaurant

import json


class TestFindRestaurant(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.fake_groups()

    def test_find_restaurant_for_group(self):
        client = Client()
        user1, user2 = User.objects.all().order_by('id')[:2]

        client.force_login(user1)
        client.post('/api/user/preferences', {
            'price': '1',
            'freeDelivery': 'false',
            'selectedCuisines': ['Brasileira'],
            'rejectedCuisines': ['Variada'],
            'rating': '0',
        })

        client.force_login(user2)
        client.post('/api/user/preferences', {
            'price': '1',
            'freeDelivery': 'true',
            'selectedCuisines': [],
            'rejectedCuisines': [],
            'rating': '2',
        })

        group = Group.objects.get(name='Só no back-end')
        r = client.get('/api/find_restaurant', {
            'id': group.id,
            'name': group.name,
        })

        self.assertEqual(r.status_code, 200)

        restaurant_slug = json.loads(r.content.decode('utf-8'))['data']
        restaurant = Restaurant.objects.get(slug=restaurant_slug)

        self.assertEqual(restaurant.cuisine.name, 'Brasileira')
        self.assertEqual(restaurant.delivery_fee, 0)
        self.assertGreaterEqual(restaurant.rating, 2)
