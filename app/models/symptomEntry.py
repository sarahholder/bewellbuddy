from django.db import models
from .entry import Entry
from .symptom import Symptom

class SymptomEntry(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, default=None, related_name="symptoms")
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE, default=None)

