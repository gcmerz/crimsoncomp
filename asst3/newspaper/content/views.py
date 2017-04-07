from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import Article


def index(request):
    return render(request, 'index.html')

def articles(request):
  latest_article_list = Article.objects.order_by('-pub_date')
  context = {'articles': latest_article_list}
  return render(request, 'articles.html', context)


def article(request, pk):
  article = get_object_or_404(Article, pk=pk)
  return render(request, 'article.html', {'article': article})
