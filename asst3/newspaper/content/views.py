from django.shortcuts import render, get_object_or_404
from models import Article, Contributor


def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')
    context = {'articles': latest_article_list}
    return render(request, 'index.html', context)

def articles(request):
    latest_article_list = Article.objects.order_by('-pub_date')
    context = {'articles': latest_article_list}
    return render(request, 'articles.html', context)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})

# Create your views here.
