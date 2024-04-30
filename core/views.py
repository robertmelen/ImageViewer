from django.shortcuts import render
from .forms import URLForm
from newspaper import Article
from django.http import HttpResponse


def image_extraction(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            article = Article(url)
            article.download()
            article.parse()
            date = article.publish_date
            all_images = article.images
            return render(request, "results.html", {'all_images': all_images, 'url': url})
    else:
        form = URLForm
        return render(request, "index.html", { 'form': form } )