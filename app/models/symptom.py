from django.db import models

class Symptom(models.Model):

    name = models.CharField(max_length=50)
    icon = models.ImageField()
    color = models.CharField(max_length=50)