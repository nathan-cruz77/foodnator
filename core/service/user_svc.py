from core.models import User


def search(user, query):
    if query is None:
        return []

    db_query = User.objects.filter(username__icontains=query).exclude(username=user.username)
    return [u.username for u in db_query.all()[:20]]
