from django.contrib import admin

# Register your models here.

from .models import Article, Contributor

admin.site.register(Article)
admin.site.register(Contributor)
