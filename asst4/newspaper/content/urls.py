from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.HomePage, name='home'),
    url(r'^articles/([a-zA-Z\d+!$@%^&();:<>\"\'.]+)/$', views.Articles, name='article'),
    url(r'^tinymce/', include('tinymce.urls')),
]