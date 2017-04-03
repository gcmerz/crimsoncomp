from django.shortcuts import render
from django.http import HttpResponse
from models import Article


def index(request):
    return render(request, 'index.html')

def articles(request):
    posts = Article.objects.all()
    articles = {'article': article}
    return render(request, 'articles.html', articles)

