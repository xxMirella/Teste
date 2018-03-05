from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^$', views.lista_posts, name='lista_posts'),
    url(r'^post/(?P<pk>\d+)/$', views.detalhes_post, name='detalhes_post'),
    url(r'^post/$', views.novo_post, name='novo_post'),
    url(r'^post/(?P<pk>\d+)/editar/$', views.editar_post, name='editar'),
    url(r'^logar/$', auth_views.login, {'template_name': 'blog/login.html'}, name='logar')
]
