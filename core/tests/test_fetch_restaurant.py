from django.test.client import Client
from django.test.testcases import TestCase

from core.models import Restaurant

import json


class TestFetchRestaurant(TestCase):
    def test_fetch_restaurant(self):
        restaurant = Restaurant.objects.first()

        client = Client()
        r = client.get('/api/restaurant/{}'.format(restaurant.slug))
        self.assertEqual(r.status_code, 200)

        restaurant_data = json.loads(r.content.decode('utf-8'))

        self.assertEqual(restaurant.name, restaurant_data['name'])
        self.assertEqual(str(restaurant.delivery_fee), restaurant_data['delivery_fee'])
        self.assertEqual(str(restaurant.rating), restaurant_data['rating'])
        self.assertEqual(restaurant.slug, restaurant_data['slug'])
        self.assertEqual(restaurant.cuisine.name, restaurant_data['cuisine'])
        self.assertEqual(restaurant.price_range.to_int(), restaurant_data['price_range'])
        self.assertEqual(restaurant.avatar, restaurant_data['avatar'])
