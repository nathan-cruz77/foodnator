from core.models import Preference
from core.models import Cuisine
from core.models import PriceRange

import json


def update(user, preferences):
    user_preference = getattr(user, 'preference', None)

    if user_preference is not None:
        user_preference.delete()

    p = Preference(
        min_rating=preferences['rating'],
        only_free_delivery=json.loads(preferences['freeDelivery']),
        price_range=PriceRange.from_int(int(preferences['price'])),
        user=user
    )
    p.save()

    if preferences.getlist('selectedCuisines', None):
        cuisines = Cuisine.objects.filter(name__in=preferences.getlist('selectedCuisines'))
        p.selected_cuisines.add(*cuisines.all())

    if preferences.getlist('rejectedCuisines', None):
        cuisines = Cuisine.objects.filter(name__in=preferences.getlist('rejectedCuisines'))
        p.rejected_cuisines.add(*cuisines.all())
