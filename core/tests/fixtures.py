from core.models import User
from core.models import Group


def user_jon():
    return User.objects.create_user(
        username='jon',
        first_name='Jon',
        last_name='Snow',
        email='jon@example.com',
        password='snow',
    )


def fake_users(n=1):
    users = []

    for i in range(n):
        users.append(User.objects.create_user(
            username='bla{}'.format(i),
            password='xablau{}'.format(i)
        ))

    return users


def fake_groups():
    u1, u2, u3 = fake_users(3)

    groups = [
        {'name': 'Grupão doido', 'users': [u1, u3]},
        {'name': 'Só no back-end', 'users': [u1, u2]},
        {'name': 'Todo mundo null', 'users': [u2, u3]},
    ]

    saved_groups = []
    for group in groups:
        g = Group(name=group['name'])
        g.save()
        g.users.add(*group['users'])
        saved_groups.append(g)

    return saved_groups
