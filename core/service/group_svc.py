from core.models import Group
from core.models import User


def list_groups(user):
    return [{'name': g.name, 'id': g.id} for g in user.group_set.all()]


def new(user, group_data):
    name = group_data.get('name')
    usernames = group_data.getlist('users') + [user.username]

    selected_users = User.objects.filter(username__in=usernames).all()

    new_group = Group(name=name)
    new_group.save()
    new_group.users.add(*selected_users)
