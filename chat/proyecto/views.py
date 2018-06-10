# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.shortcuts import render

from django.http import HttpResponse
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.template import loader

from .forms import ContactForm, FilesForm, ContactFormSet, SignUpForm
from .models import Post, User
import datetime

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect




usuario = None

def index(request):

    return render(request, 'profile.html')


def inicioSesion(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        global usuario
        usuario = User.objects.get(username=username)
        latest_question_list = Post.objects.filter(usuario=usuario)
        template = loader.get_template('proyecto/perfil.html')
        context = {
            'latest_question_list': latest_question_list,
        }
        return HttpResponse(template.render(context, request))

    else:
        return render(request, 'profile.html')

def message(request):
    return render(request, 'proyecto/messages.html')

class DefaultFormView(FormView):
    template_name = 'proyecto/form.html'
    form_class = ContactForm

def enviarMensaje(request):
    titulo = request.POST['titulo']
    texto = request.POST['message']

    global usuario
    m = Post(texto=texto, titulo=titulo,usuario = usuario, date = datetime.datetime.now())
    m.save()
    latest_question_list = Post.objects.order_by('date')[:5]
    template = loader.get_template('proyecto/perfil.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'proyecto/signup.html', {'form': form})