from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.lista_posts, nome='Lista_posts')
]
