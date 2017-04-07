from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def articles(request):
	latest_article_list = Articles.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/articles.html')
	context = {
        'latest_article_list': latest_article_list,
    }
	return render(request, 'articles.html', {})

def article(request):
	return render(request, 'article.html', {})