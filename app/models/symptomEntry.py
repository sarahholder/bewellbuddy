from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .symptom import Symptom

class symptomEntry(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    comments = models.Charfield(max_length=250)
    entry_date = models.DateField(default=datetime.now())
    
