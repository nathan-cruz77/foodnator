from core.models import Group

def list_groups(user):
    return [{'name': g.name, 'id': g.id} for g in user.group_set.all()]
