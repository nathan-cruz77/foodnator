from core.models import User


def search(query):
    return [u.username for u in User.objects.filter(username__icontains=query).all()[:20]]
