from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import datetime
from app.models import Medicine

@login_required
def medicine_form(request):
    if request.method == 'GET':
        todays_date = datetime.date.today().strftime("%Y-%m-%d")
        context = {
            'todays_date': todays_date
        }
        return render(request, 'medicines/form.html', context)

def update_medicine_form(request, medicine_id):
    form_data = request.POST
    medicine = Medicine.objects.get(pk=medicine_id)

    if request.method == 'GET':
        context = { 
            'medicine': medicine
        }

        return render(request, 'medicines/form.html', context)

