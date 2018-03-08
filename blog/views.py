# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from blog.models import Post
from .forms import PostForm
from .models import InfoUsuario

# Create your views here.


def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista_post.html', {'posts': posts})


def detalhes_post(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalhes_post.html', {'posts': posts})


def editar_post(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    forms = PostForm(request.POST or None, instance=posts)

    if request.method == "POST":
        if forms.is_valid():
            post = forms.save(commit=False) #TODO: testar apenas com o form.instance
            post.autor = request.user #TODO: passar o user para a instancia do form
            post.data_publicacao = timezone.now()
            post.save()
            return redirect('detalhes_post', pk=post.pk)

    return render(request, 'blog/form.html', {'forms': forms})


def novo_post(request):
    #TODO: usar o messages do django
    forms = PostForm(request.POST or None)

    if request.method == "POST":
        if forms.is_valid():
            post = forms.save(commit=False)
            post.autor = request.user
            post.data_publicacao = timezone.now()
            post.save()
            return redirect('detalhes_post', pk=post.pk)

    return render(request, 'blog/form.html', {'forms': forms})


def cadastro(request):
    if request.method == 'POST':
        data = request.POST
        try:
            user = User.objects.create_user(
                username=data.get('nome_usuario'), email=data.get('email'), password=data.get('senha'),
                first_name=data.get('primeiro_nome'), last_name=data.get('ultimo_nome'))

        except Exception as err:
            return render(request, 'blog/cadastro.html', {'message': 'error'})
        InfoUsuario.objects.create(user=user)
        login(request, user)
        return redirect('lista_posts')

    else:
        return render(request, 'blog/cadastro.html')


def logar(request):
    if request.method == 'POST':
        data = request.POST
        usuario = authenticate(username=data.get('nome_usuario'), password=data.get('senha'))

        if usuario is not None:
            login(request, usuario)
            return redirect('lista_posts')

        else:
            return render(request, 'blog/login.html')

    else:
        return render(request, 'blog/login.html')


def deslogar(request):
    logout(request)
    return redirect('lista_posts')

