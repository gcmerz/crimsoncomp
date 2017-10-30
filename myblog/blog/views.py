# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import Post
from django.shortcuts import get_object_or_404, render

# Create your views here.
def get_post(request, post_id):
	# fetch the blog post objects from the database
	post_obj = get_object_or_404(Post, pk=post_id)
	# pass to a template that displays a single blog post
	return render(request, 'single_post.html', {'post': post_obj})