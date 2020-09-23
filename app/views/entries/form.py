from django import forms
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
import datetime
from app.models import Symptom, Entry, SymptomEntry

@login_required
def entry_form(request):
    form_data = request.POST

    if request.method == 'GET':
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
    entry_symptoms = SymptomEntry.objects.filter(entry=entry)
    todays_date = datetime.date.today().strftime("%Y-%m-%d")
    selected_symptoms= []

    for entry_symptom in entry_symptoms:
        
        for symptom in symptoms: 
            if entry_symptom.symptom_id == symptom.id: 
                selected_symptoms.append(symptom)
    
                print(symptom.id)

    print(selected_symptoms)

    if request.method == 'GET':        
        context = {
            'entry': entry,
            'symptoms': symptoms,
            'todays_date': todays_date,
            'selected_symptoms': selected_symptoms
        }
        return render(request, 'entries/form.html', context)


    
    elif request.method == 'POST':
        checked_symptoms = request.POST.getlist('symptoms')
        
        print(form_data)
        entry.entry_date = form_data['entry_date']
        entry.comments = form_data['comments']
        entry.save()

        entry_symptoms = entry_symptoms.filter(entry=entry)
        

        for entry_symptom in entry_symptoms:
            entry_symptom.delete()


        for symptom in checked_symptoms:
            SymptomEntry.objects.create(
            entry = entry,
            symptom_id = symptom
        )

        return render(request, "entries/list.html")

    
    
        


        

