from django import forms
from django.shortcuts import render
from app.models import Symptom
import datetime

def entry_form(request):
    if request.method == 'GET':
        symptoms = Symptom.objects.all()
        template = 'entries/form.html'
        todays_date = datetime.date.today().strftime("%Y-%m-%d")
        context = {
            'symptoms': symptoms,
            'todays_date': todays_date
        }
        return render(request, template, context)




        

