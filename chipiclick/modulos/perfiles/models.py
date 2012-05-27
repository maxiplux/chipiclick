# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django_facebook.models import FacebookProfileModel


class Perfil(FacebookProfileModel):
    user = models.OneToOneField('auth.User')