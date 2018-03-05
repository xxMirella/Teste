# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from blog.models import Post
from .forms import PostForm
from .forms import LoginForm

# Create your views here.


def lista_posts(request):
    posts = Post.objects.filter(data_publicacao__lte=timezone.now())
    return render(request, 'blog/lista_post.html', {'posts': posts})


def detalhes_post(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalhes_post.html', {'posts': posts})


def editar_post(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        forms = PostForm(request.POST, instance=posts)
        if forms.is_valid():
            post = forms.save(commit=False)
            post.autor = request.user
            post.data_publicacao = timezone.now()
            post.save()
            return redirect('detalhes_post', pk=post.pk)
    else:
        forms = PostForm(instance=posts)
    return render(request, 'blog/form.html', {'forms': forms})

def novo_post(request):
    if request.method == "POST":
        forms = PostForm(request.POST)
        if forms.is_valid():
            post = forms.save(commit=False)
            post.autor = request.user
            post.data_publicacao = timezone.now()
            post.save()
            return redirect('detalhes_post', pk=post.pk)
    else:
        forms = PostForm()
    return render(request, 'blog/form.html', {'forms': forms})


def logar(request):
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            usuario = authenticate(nome_usuario=cd['nome_usuario'], senha=['senha'])
            if usuario is not None:
                if usuario.is_active:
                    login(request, usuario)
                    return redirect('lista_posts')
                else:
                    return HttpResponse('Conta desabilitada')
            else:
                return HttpResponse('Login Invalido')
    else:
        forms = LoginForm()
    return render(request, 'blog/login.html', {'forms': forms})
