# -*- coding: utf-8 -*-
from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'text')

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if len(titulo) < 3:
            raise forms.ValidationError("O título deve conter mais de 3 letras")
        return titulo