# -*- coding: utf-8 -*-

from django.db import models



# the following lines added:
import datetime
from django.utils import timezone



class User(models.Model):
        username = models.CharField(max_length=20)
        password = models.CharField(max_length=20)
        clavepublica_d = models.BigIntegerField()
        clavepublica_e = models.BigIntegerField()
        phi =  models.BigIntegerField()


class Post(models.Model):
    texto = models.CharField(max_length=2000)
    date = models.DateField
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


# Create your models here.
