from django.shortcuts import render
from django.http import HttpResponse

from .forms import ArticleForm


# def index(request):
#     return HttpResponse("Hello, world. You're at the ui index.")


def article_create(request):
    article_form = ArticleForm()
    return render(request, "ui/article_form.html", {"form": article_form})
