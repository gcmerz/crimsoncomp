# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from models import Article, Contributor

# Create your views here.
def get_article(request, article_id):
	art_obj = get_object_or_404(Article, pk=article_id)
	return render(request, 'single_article.html',{'article':art_obj})

def get_homepage(request):
	return render(request, 'index.html', {'articles':Article.objects.all()})

