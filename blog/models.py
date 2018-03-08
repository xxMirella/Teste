# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    autor = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    text = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(default=timezone.now, null=False)

    class Meta:
        ordering = ['-data_publicacao',]

    def publicar(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return "id: %s - titulo: %s" % (self.id, self.titulo)


class InfoUsuario(models.Model):
    user = models.ForeignKey(User)
