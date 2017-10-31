from django.contrib import admin

from .models import Article

from .models import Contributor

admin.site.register(Article)
admin.site.register(Contributor)
# Register your models here.
