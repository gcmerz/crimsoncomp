from django.shortcuts import render

# code taken from https://tutorial.djangogirls.org/en/django_views/
def post_list(request):
    return render(request, 'blog/post_list.html', {})
