from __future__ import unicode_literals
from django.db import models

class Movie(models.Model):
    url = models.TextField(null=True)
    content = models.TextField(null=True)

class Weather(models.Model):
    day = models.TextField(null=True)
    weather = models.TextField(null=True)
    temp = models.TextField(null=True)

class JDphone(models.Model):
    item_page = models.TextField(null=True)
    item_name = models.TextField(null=True)
    item_price = models.TextField(null=True)