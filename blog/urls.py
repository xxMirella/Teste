from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.lista_posts, name='Lista_posts'),
    url(r'^post/(?P<pk>\d+)/$', views.detalhes_post, name='detalhes_post')
]
