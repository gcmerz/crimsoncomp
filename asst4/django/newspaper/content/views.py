# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from models import Content, Article, Contributor

# Create your views here.
def get_content(request, content_id):
    content_obj = get_object_or_404(Article, pk=content_id)
    return render(request, 'template.html', {'content': content_obj})
def get_home(request):
	return render(request, 'home.html')
