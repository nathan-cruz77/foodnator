# coding: utf-8
import json

from django.contrib import auth
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError

from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required

from core.service import log_svc
from core.service import cuisine_svc
from core.service import group_svc
from core.service import preference_svc
from core.service import restaurant_svc
from core.service import user_svc


def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated():
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated() else {'authenticated': False}
    return JsonResponse(i_am)


def list_cuisines(request):
    return JsonResponse({'data': cuisine_svc.list_cuisines()})


@ajax_login_required
def list_groups(request):
    return JsonResponse({'data': group_svc.list_groups(request.user)})


@ajax_login_required
def preferences(request):
    if request.method == 'POST':
        try:
            preference_svc.update(request.user, request.POST)
        except IntegrityError:
            print('Trying to insert preference without deleting the previous one')
        finally:
            return JsonResponse({})

    if request.method == 'GET':
        return JsonResponse(preference_svc.load(request.user))


@ajax_login_required
def find_restaurant(request):
    return JsonResponse({'data': restaurant_svc.find(request.user, request.GET)})


def fetch_restaurant(request, slug=''):
    if slug == 'not-found':
        return JsonResponse({}, status=404)
    return JsonResponse(restaurant_svc.fetch(slug))


@ajax_login_required
def search_users(request):
    data = user_svc.search(request.user, request.GET.get('query'))
    return JsonResponse({'data': data})


@ajax_login_required
def new_group(request):
    data = group_svc.new(request.user, request.POST)
    return JsonResponse({})


def create_user(request):
    return JsonResponse(user_svc.new(request.POST))


def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d
