from core.models import User


def search(user, query):
    db_query = User.objects.filter(username__icontains=query).exclude(username=user.username)
    return [u.username for u in db_query.all()[:20]]
