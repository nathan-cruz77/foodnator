from core.models import Cuisine


def list_cuisines():
    return [c.name for c in Cuisine.objects.all()]
