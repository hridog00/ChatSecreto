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

from .forms import ContactForm, FilesForm, ContactFormSet


def index(request):

    return render(request, 'profile.html')


def inicioSesion(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'proyecto/perfil.html')

    else:
        return render(request, 'profile.html')

class DefaultFormView(FormView):
    template_name = 'proyecto/form.html'
    form_class = ContactForm
