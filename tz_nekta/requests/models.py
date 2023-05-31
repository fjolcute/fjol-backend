from django.contrib import auth
from django.contrib.auth.forms import *
from django.db import models
from django.urls import *
from django.views.generic import *
from django.contrib.auth.models import User
from django.conf import settings



class Request(models.Model):
    request = models.TextField(blank=True, verbose_name='Заявка')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)


class RequestMessage(models.Model):
    reqmail = models.TextField(blank=True, verbose_name='Содержание заявки')
    request = models.TextField(blank=True, verbose_name='id заявки')


