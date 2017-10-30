from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
from .models import Content, Contributor, Article

admin.site.register(Content)
admin.site.register(Contributor)
class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }
admin.site.register(Article,ArticleAdmin)