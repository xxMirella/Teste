# -*- coding: utf-8 -*-
from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'text')


class LoginForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=30)
    ultimo_nome = forms.CharField(label='Ultimo nome', max_length=60)
    email = forms.EmailField(label='Email', max_length=200)
    nome_usuario = forms.CharField(label='Nome de usuario', max_length=30)
    senha = forms.CharField(widget=forms.PasswordInput)

