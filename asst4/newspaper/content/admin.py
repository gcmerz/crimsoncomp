from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE

# Register your models here.

from .models import Article, Contributor

class ArticleAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})}
	}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Contributor)
