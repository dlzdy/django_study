# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import models
# Create your views here.


def test(request):
    # return HttpResponse('Hello,world')
    article = models.Article.objects.get(pk=1)
    #return render(request, "blog/index.html", {"hello": "hello blog"})
    return render(request, "blog/test.html", {"article": article})


def index(request):
    # return HttpResponse('Hello,world')
    articles = models.Article.objects.all()
    #return render(request, "blog/index.html", {"hello": "hello blog"})
    return render(request, "blog/index.html", {"articles": articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, "blog/article_page.html", {"article": article})


# http://localhost:8000/blog/edit/1
def edit_page(request, article_id):
    if str(article_id) == "0":
        return render(request, "blog/edit_page.html")
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request, "blog/edit_page.html", {"article": article})


def edit_action(request):
    title = request.POST.get("title", "TITLE");
    content = request.POST.get("content", "CONTENT");
    models.Article.objects.create(title=title, content=content)
    articles = models.Article.objects.all()
    return render(request, "blog/index.html", {"articles": articles})