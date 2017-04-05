from django.contrib import admin

from .models import Article
from .models import Contributor

class ArticleAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'title', 'subtitle', 'contributors', 'text']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Contributor)