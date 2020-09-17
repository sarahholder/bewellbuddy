from django.db import models
from django.contrib.auth.models import User
from .symptom import Symptom

class Entry(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_date = models.DateField(null=True, blank=True, auto_now=True)
    comments = models.CharField(max_length=250, blank=True, null=True)
    
