# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from models import Content

# Create your views here.
def get_content(request, content_id):
    content_obj = get_object_or_404(Content, pk=content_id)
    return render(request, 'template.html', {'Content': Content_obj})