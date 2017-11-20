from __future__ import unicode_literals
from django.shortcuts import render
from django.views import generic
from .models import Article, Contributor

num_articles=Article.objects.all().count()
num_authors=Contributor.objects.all().count()


def index(request):
    
	
    
	output = []
    pos = 0
	temp = []
    for a in Article.objects.all():
        temp.append(str(a.title))
		
        temp.append("http://127.0.0.1:8000/page/article/"+str(pos + 1) )
        output.append(temp)
        temp = []
        pos += 1
		
		
    return render(
        request, 'index.html', context={'data':output,'num_authors':num_authors,'num_articles':num_articles},
    )

def articleListView(request, pk):

    ipk = int(pk)-1
    if ipk < num_articles:
        articleObject = Article.objects.all()[ipk]
        contributors = ""
		
        for element in articleObject.contributors.all():
		
            contributors += str(element.show())
            contributors += ', '
        contributors = contributors[:-2]
        return render(
		
            request,
            'article_template.html',
            context={'contributors':contributors,'title':articleObject.title,'subtitle':articleObject.subtitle,'date':articleObject.pub_date,'text':articleObject.text},
        )
    else:
        return render(
            request,
            'not_found.html',
            context={'num_articles':num_articles},
        )
