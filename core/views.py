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
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
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