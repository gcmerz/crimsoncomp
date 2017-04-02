from django.contrib import admin

# Register your models here.
from .models import Article, Contributor

class ArticleText(admin.ModelAdmin):
    fields = ['title', 'subtitle', 'text', 'pub_date', 'contributors']

admin.site.register(Article, ArticleText)
admin.site.register(Contributor)