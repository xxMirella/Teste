# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from blog.models import Post
from .forms import PostForm

# Create your views here.


def lista_posts(request):
    posts = Post.objects.filter(data_publicacao__lte=timezone.now())
    return render(request, 'blog/lista_post.html', {'posts': posts})


def detalhes_post(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalhes_post.html', {'posts': posts})


def novo_post(request):
    forms = PostForm()
    return render(request, 'blog/form.html', {'forms': forms})

