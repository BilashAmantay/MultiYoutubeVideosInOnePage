from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlencode

from .forms import ArticleForm


# def index(request):
#     return HttpResponse("Hello, world. You're at the ui index.")


def article_create(request):
    if request.method == "POST":
        base_url = 'embed'
        youtube_urls = '-'.join([ request.POST['URL1'], request.POST['URL2'] ])
        url = '{}/{}/'.format(base_url, youtube_urls) 
        return HttpResponseRedirect(url)


    article_form = ArticleForm(initial={"URL1":"sGkh1W5cbH4", "URL2":"ldiaiDt1w9g"})
    return render(request, "ui/article_form.html", {"form": article_form})


def embed(request,urls):
    if request.method == "GET":
        print('got post')
        print(urls)
        URLS = urls.split('-')
        print('URLS', URLS)

    return render(request, "ui/embed.html",{'URLS' : URLS})