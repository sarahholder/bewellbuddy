from django import forms
from django.shortcuts import render, redirect, reverse
from app.models import Symptom, Entry, SymptomEntry
import datetime

def entry_form(request):
    form_data = request.POST

    if request.method == 'POST':
        symptoms = Symptom.objects.all()
        template = 'entries/form.html'
        todays_date = datetime.date.today().strftime("%Y-%m-%d")
        checked_symptoms = request.POST.getlist('symptoms')

        context = {
            'symptoms': symptoms,
            'todays_date': todays_date
        }

        new_entry = Entry.objects.create(
            user = request.user,
            entry_date = form_data['new_entry_date'],
            comments = form_data['comments']
        )

        for symptom in checked_symptoms:
            SymptomEntry.objects.create(
                entry = new_entry,
                symptom_id = symptom
            )

        return redirect(reverse('app:entries'))

    elif request.method == 'GET':
        template = 'entries/form.html'
        symptoms = Symptom.objects.all()
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
 
        entry.entry_date = form_data['entry_date']
        entry.comments = form_data['comments']
        entry.save()

        entry_symptoms = entry_symptoms.filter(entry=entry)
        print(entry_symptoms)

        for entry_symptom in entry_symptoms:
            entry_symptom.delete()


        for symptom in checked_symptoms:
            SymptomEntry.objects.create(
            entry = entry,
            symptom_id = symptom
        )

        return render(request, "entries/list.html")

    
    
        


        

