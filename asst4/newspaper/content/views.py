from django.shortcuts import render
import datetime

def post_list(request):
    return render(request, 'newspaper/article.html', {})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):



# Create your views here.
