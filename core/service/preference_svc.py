from core.models import Preference
from core.models import Cuisine
from core.models import PriceRange

import json


def update(user, preferences):
    if hasattr(user, 'preference'):
        user.preference.delete()

    p = Preference(
        min_rating=preferences['rating'],
        only_free_delivery=json.loads(preferences['freeDelivery']),
        price_range=PriceRange.from_int(int(preferences['price'])),
        user=user
    )
    p.save()

    if preferences.get('selectedCuisines', None):
        selected_cuisines = preferences.get('selectedCuisines').split(',')
        cuisines = Cuisine.objects.filter(name__in=selected_cuisines)
        p.selected_cuisines.add(*cuisines.all())

    if preferences.get('rejectedCuisines', None):
        rejected_cuisines = preferences.get('rejectedCuisines').split(',')
        cuisines = Cuisine.objects.filter(name__in=rejected_cuisines)
        p.rejected_cuisines.add(*cuisines.all())


def load(user):
    user_preference = getattr(user, 'preference', None)

    if user_preference is None:
        return {
            'price': 1,
            'freeDelivery': False,
            'selectedCuisines': [],
            'rejectedCuisines': [],
            'rating': 0,
        }

    return {
        'price': user_preference.price_range.to_int(),
        'freeDelivery': user_preference.only_free_delivery,
        'selectedCuisines': [c.name for c in user_preference.selected_cuisines.all()],
        'rejectedCuisines': [c.name for c in user_preference.rejected_cuisines.all()],
        'rating': float(user_preference.min_rating),
    }
