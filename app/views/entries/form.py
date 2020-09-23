from django import forms
from django.shortcuts import render, redirect
from app.models import Symptom, Entry, SymptomEntry
import datetime

def entry_form(request):
    form_data = request.POST

    if request.method == 'GET':
        symptoms = Symptom.objects.all()
        template = 'entries/form.html'
        todays_date = datetime.date.today().strftime("%Y-%m-%d")
        context = {
            'symptoms': symptoms,
            'todays_date': todays_date
        }
        
        return render(request, template, context)



def update_entry_form(request, entry_id):
    form_data = request.POST
    symptoms = Symptom.objects.all() 
    entry = Entry.objects.get(pk=entry_id)
    entry_symptoms = SymptomEntry.objects.all()
    todays_date = datetime.date.today().strftime("%Y-%m-%d")

    if request.method == 'GET':
                 
        context = {
            'entry': entry,
            'symptoms': symptoms,
            'todays_date': todays_date
        }
        return render(request, 'entries/form.html', context)
    
    elif request.method == 'POST':
        checked_symptoms = request.POST.getlist('symptoms')

        new_entry = Entry.objects.create(
            user = request.user,
            entry_date = form_data['entry_date'],
            comments = form_data['comments']
        )

        for symptom in checked_symptoms:
            SymptomEntry.objects.create(
                entry = new_entry,
                symptom_id = symptom
            )

            return render(request, "entries/list.html", context)

    
    
        


        

