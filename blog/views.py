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
    articles = models.Article.objects.all()
    #return render(request, "blog/index.html", {"hello": "hello blog"})
    return render(request, "blog/index.html", {"articles": articles})

def article_page(request, article_id):
    article = models.Article.objects.get(pk = article_id)
    return render(request, "blog/article_page.html", {"article": article})
    #return render(request, "blog/article_page.html",{"hello": "hello blog"})