from django.conf import settings
from django.db import models
class Scar(models.Model):
    'Generated Model'
    scarName = models.CharField(max_length=256,)
    wigField = models.CharField(max_length=256,null=True,blank=True,)
