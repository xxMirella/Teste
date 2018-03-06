from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.lista_posts, name='lista_posts'),
    url(r'^post/(?P<pk>\d+)/$', views.detalhes_post, name='detalhes_post'),
    url(r'^post/$', views.novo_post, name='novo_post'),
    url(r'^post/(?P<pk>\d+)/editar/$', views.editar_post, name='editar'),
    url(r'^logar$', views.logar, name='logar'),
    url(r'^deslogar/$', views.deslogar, name='deslogar'),
    url(r'^cadastro/$', views.cadastro, name='cadastro'),
]
