from django.shortcuts import render
from django.http import Http404

from .models import Article

def index(request):
	latest_articles = Article.objects.order_by('-pub_date')[:5]
	context = {'latest_articles': latest_articles} 
	return render(request, 'articles/index.html', context)

def article(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("oohhh no WHAT ARE YOU DOING")
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

def detail(request, article_id):
	return HttpResponse("You're looking at article %s." % article_id)
