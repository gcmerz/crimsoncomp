from django.contrib import admin
# from https://docs.djangoproject.com/en/1.8/intro/tutorial02/#creating-an-admin-user

from .models import Content 
admin.site.register(Content)