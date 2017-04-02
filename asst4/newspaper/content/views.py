from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article, Contributor

# Create your views here.
def HomePage(request):
    articles = Article.objects.all()
    return render(request, 'content/index.html', {'articles' : articles})

def Articles(request, article_title):
    article = Article.objects.get(title=article_title)
    authors = article.contributors.all()

    names = list()
    for author in authors:
        names.append(author.first_name + ' ' + author.last_name)
    
    return render(request, 'content/article.html', {'article' : article, 'authors' : names})