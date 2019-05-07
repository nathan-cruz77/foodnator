from core import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/dapau$', views.dapau),
    url(r'^api/login$', views.login),
    url(r'^api/logout$', views.logout),
    url(r'^api/whoami$', views.whoami),

    url(r'^api/cuisines$', views.list_cuisines),
    url(r'^api/groups$', views.list_groups),
    url(r'^api/user/preferences$', views.preferences),
    url(r'^api/find_restaurant$', views.find_restaurant),
    url(r'^api/restaurant/(?P<slug>[\w-]+)$', views.fetch_restaurant),
    url(r'^api/users/search$', views.search_users),
    url(r'^api/group/new', views.new_group),
]
