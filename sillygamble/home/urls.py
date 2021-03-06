from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^howto/$', views.howto), # Change to "instructions".
    url(r'^about/$', views.about),
    url(r'^games/$', views.games),
    url(r'^trust/$', views.trust),
    url(r'^responsable/$', views.responsable), # Change to "responsible".
]
