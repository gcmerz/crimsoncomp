# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import Content, Article, Contributor
from django.shortcuts import get_object_or_404, render

# Create your views here.
def get_content(request, content_id):
	content_obj = get_object_or_404(Article, pk=content_id)
	return render(request, 'content.html', {'article': content_obj})
def get_home(request):
	return render(request, 'home.html')