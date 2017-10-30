from django.shortcuts import render
from .models import Article, Contributor, Content
# Create your views here.
def article(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	return render(request, 'content/articles.html', {'article':article})
def home(request):
	articles = Article.objects.all()
	return render(request, 'content/home.html', {'articles':articles})