from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^article/(\d)/+$', views.article, name='article'),
    url(r'^home/$', views.home, name='home')
]