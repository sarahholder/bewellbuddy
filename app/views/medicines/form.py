from django import forms
from django.shortcuts import render
from app.models import Medicine
import datetime

def medicine_form(request):
    if request.method == 'GET':
        todays_date = datetime.date.today().strftime("%Y-%m-%d")
        context = {
            'todays_date': todays_date
        }
        return render(request, 'medicines/form.html', context)
