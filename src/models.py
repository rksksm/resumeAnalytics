# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class JD(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=3000)
    isActive = models.BooleanField(default='True')