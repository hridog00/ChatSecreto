# -*- coding: utf-8 -*-

from django.db import models



# the following lines added:
import datetime
from django.utils import timezone

class Question(models.Model):
   question_text = models.CharField(max_length=200)
   pub_date = models.DateTimeField('date published')

   def __str__(self):
       return self.question_text

   def was_published_recently(self):
       now = timezone.now()
       return now - datetime.timedelta(days=1) <= self.pub_date <= now

   was_published_recently.admin_order_field = 'pub_date'
   was_published_recently.boolean = True
   was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING,)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


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
