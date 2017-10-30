from django.contrib import admin
# Register your models here.
from .models import Content, Contributor, Article

admin.site.register(Content)
admin.site.register(Contributor)
admin.site.register(Article)