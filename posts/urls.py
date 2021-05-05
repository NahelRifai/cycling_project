from django.urls import path
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$',views.post_list, name="list"),
    url(r'^create/$',views.post_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name="detail"),
]

urlpatterns += staticfiles_urlpatterns()