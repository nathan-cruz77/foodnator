import random

from core.models import Group
from core.models import Restaurant


def find(group_data):
    group = Group.objects.get(id=group_data['id'])
    preferences = [u.preference for u in group.users.all() if hasattr(u, 'preference')]

    min_rating = max(p.min_rating for p in preferences)
    max_price = min(p.price_range for p in preferences)
    only_free_delivery = any(p.only_free_delivery for p in preferences)


    selected_cuisines = set()
    rejected_cuisines = set()
    for p in preferences:
        selected_cuisines.update(p.selected_cuisines.all())
        rejected_cuisines.update(p.rejected_cuisines.all())

    q = Restaurant.objects.filter(
        rating__gte=min_rating,
        price_range__lte=max_price
    )

    if only_free_delivery:
        q = q.filter(delivery_fee=0)

    if selected_cuisines:
        q = q.filter(cuisine__in=selected_cuisines)

    if rejected_cuisines:
        q = q.exclude(cuisine__in=rejected_cuisines)

    result = q.all()

    if not result:
        return 'not-found'

    return random.choice(result).slug
