from django import forms
from django.shortcuts import render
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

def edit_entry_form(request, entry_id):
    if request.method == 'GET':
        template = 'entries/form.html'
        return render(request, template)
    
    if request.method == 'POST':
        entry = Entry.objects.get(pk=entry_id) 
        entry_symptoms = SymptomEntry.objects.all()
        entrydate = entry.entry_date
        todays_date = datetime.date.today().strftime("%Y-%m-%d")
        for entry_symptom in entry_symptoms:
            if(entry_symptom.id == entry_id):
                symptoms = []
                symptoms.append(entry_symptom)
                
                context = {
                    'entry': entry,
                    'symptoms': symptoms,
                    'entrydate': entrydate, 
                    'todays_date': todays_date

                }
                return render(request, "entries/list.html", context)
        

        
        





        

