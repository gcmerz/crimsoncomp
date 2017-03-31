from django.shortcuts import render
from django.utils import timezone
from .models import Content
from django.shortcuts import render, get_object_or_404
from .forms import ContentForm
from django.shortcuts import redirect

def content_list(request):
    contents = Content.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'content/content_list.html', {'contents': contents})

def content_detail(request, pk):
    content = get_object_or_404(Post, pk=pk)
    return render(request, 'content/content_detail.html', {'content': content})

def content_new(request):
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.contributors = request.user
            content.pub_date = timezone.now()
            content.save()
            return redirect('content_detail', pk=content.pk)
    else:
        form = ContentForm()
    return render(request, 'content/content_edit.html', {'form': form})

def content_edit(request, pk):
    content = get_object_or_404(Content, pk=pk)
    if request.method == "POST":
        form = Content(request.POST, instance=content)
        if form.is_valid():
            content = form.save(commit=False)
            content.contributors = request.user
            content.pub_date = timezone.now()
            content.save()
            return redirect('content_detail', pk=content.pk)
    else:
        form = ContentForm(instance=post)
    return render(request, 'content/content_edit.html', {'form': form})
