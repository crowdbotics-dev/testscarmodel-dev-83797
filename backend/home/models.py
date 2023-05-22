from django.conf import settings
from django.db import models
class Scar(models.Model):
    'Generated Model'
    scarName = models.CharField(max_length=256,)
    wigField = models.CharField(null=True,blank=True,max_length=256,)
