from core.models import User
from core.models import Cuisine


def user_jon():
    ze = User.objects.create_user(
        username='jon',
        first_name='Jon',
        last_name='Snow',
        email='jon@example.com',
        password='snow',
    )
    return ze


def fake_cuisines():
    cuisines = [
        {'name': 'Lanches'},
        {'name': 'Brasileira'},
        {'name': 'Pizza'},
    ]

    return [Cuisine.objects.create(**cuisine) for cuisine in cuisines]
