from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from content import views

urlpatterns = [
    url(r'^post/(?P<pk>\d+)/$', views.get_article, name='posttemp'),
    url(r'^$', views.get_home, name='homepage'),
]
