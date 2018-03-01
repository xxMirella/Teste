# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def lista_posts(request):
    return render(request, 'blog/lista_post.html', {})

