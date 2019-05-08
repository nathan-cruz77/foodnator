from core.models import User


def search(user, query):
    db_query = User.objects.filter(username__icontains=query).exclude(username=user.username)
    return [u.username for u in db_query.all()[:20]]


def new(data):
    User.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
    return { 'created': True }
