from django.shortcuts import render
from .forms import URLForm
from newspaper import Article
from newspaper import Config
from django.http import HttpResponse


def image_extraction(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'
            config = Config()
            config.browser_user_agent = user_agent
            article = Article(url, config=config)
            article.download()
            article.parse()
            date = article.publish_date
            all_images = article.images
            return render(request, "results.html", {'all_images': all_images, 'url': url})
    else:
        form = URLForm
        return render(request, "index.html", { 'form': form } )