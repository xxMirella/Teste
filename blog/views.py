# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone

from blog.models import Post

# Create your views here.


def lista_posts(request):
    posts = Post.objects.filter(data_publicacao__lte=timezone.now())
    return render(request, 'blog/lista_post.html', {'posts': posts})

