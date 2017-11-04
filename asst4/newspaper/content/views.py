# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from models import Article, Contributor
# Create your views here.
def get_article(request, article_id):
    # fetch the blog post object from the database
    article_obj = get_object_or_404(Article, pk=article_id)
    # pass it to a template that displays a single blog post
    return render(request, 'article.html', {'article': article_obj})

def get_homepage(request):
	return render(request, 'homepage.html', {'articles':Article.objects.all()})