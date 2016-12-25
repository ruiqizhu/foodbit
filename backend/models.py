from __future__ import unicode_literals

from django.db import models

# Create your models here.

class FoodEvent(models.Model):
    title = models.CharField(max_length=200,default="")
    name = models.CharField(max_length=30,default="")
    location = models.CharField(max_length=50,default="", blank=True, null=True)
    time = models.CharField(max_length=50,default="", blank=True, null=True)
    organization = models.CharField(max_length=50,default="", blank=True, null=True)
    foodtype = models.CharField(max_length=50,default="", blank=True, null=True)
    description = models.CharField(max_length=50,default="", blank=True, null=True)
    image = models.CharField(max_length=500,default="")
    def __str__(self): 
        return self.title
