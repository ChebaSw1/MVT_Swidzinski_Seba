from django.db import models

class Familiares(models.Model):
    nombre= models.CharField(max_length=30)
    anios= models.CharField(max_length=30)
    parentesco= models.CharField(max_length=30)
    cumpleanios = models.CharField(max_length=30)
