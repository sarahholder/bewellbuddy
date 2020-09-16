from django.db import models
from django.utils import timezone

class Symptom(models.Model):

    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)