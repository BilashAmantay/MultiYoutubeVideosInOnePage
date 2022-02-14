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
        url = '{}/{}/'.format(base_url, request.POST['URL1']) 
        return HttpResponseRedirect(url)


    article_form = ArticleForm()
    return render(request, "ui/article_form.html", {"form": article_form})


def embed(request,url):
    print('embed view--------------')
    print(request.method)
    print(request)
    print(url)
    # {'para' : url}
    if request.method == "POST":
        print('got post')
        print(request.POST)

    return render(request, "ui/embed.html",{'URL' : url})