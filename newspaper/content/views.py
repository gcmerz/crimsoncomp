from django.shortcuts import render
from .models import Content, Article


def article(request, title):
	articles = Article.objects.all()
	print title
	chosen = articles[0]
	for a in range(len(articles)):
	    if articles[a].title == title:
	        chosen = articles[a]
	        break
	
	print chosen.title
	t = chosen.title
	print "check"
	return render(request, 'content/article.html', chosen)

def all_articles(request):
	articles = Article.objects.all() 
	return render(
		request,'content/all_articles.html', {'articles': articles})
