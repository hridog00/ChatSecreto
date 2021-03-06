from django.conf.urls import url, include
from django.contrib.auth.views import login


import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^inicioSesion$', views.inicioSesion, name='inicioSesion'),
    url(r'^signup', views.signup, name='signup'),

    url(r'^sendMessage', views.enviarMensaje, name='perfilnMessge'),
    url(r'^registro', views.registro, name='registro'),

    # url(r'^accounts/login$', 'django.contrib.auth.views.login'),
    url(r'^form$', views.DefaultFormView.as_view(), name='form_default'),
    url(r'^message', views.message, name='escribe_mensajet'),
    url(r'^descifrar/(?P<id>\d+)', views.descifrar ,name="perfilnMessge"),


]