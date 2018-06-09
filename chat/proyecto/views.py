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

from .forms import ContactForm, FilesForm, ContactFormSet
from .models import Post


def index(request):

    return render(request, 'profile.html')


def inicioSesion(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

        latest_question_list = Post.objects.order_by('-pub_date')[:5]
        template = loader.get_template('polls/index.html')
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
