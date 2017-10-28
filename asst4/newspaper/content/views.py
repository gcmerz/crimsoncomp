# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from content.models import Content
from django.shortcuts import render

# Create your views here.
def get_home(request):
	contents = Content.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
	return render(request, 'content/homepage.html', {'contents': contents})

def get_article(request, pk):
	content = get_object_or_404(Content, pk=pk)
	return render(request, 'content/posttemp.html', {'content': content})

