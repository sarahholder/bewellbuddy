from django.shortcuts import render, redirect, reverse
from app.models import Entry, SymptomEntry
from django.contrib.auth.decorators import login_required

@login_required
def entry_detail(request, entry_id):
    form_data = request.POST
    entry = Entry.objects.get(pk=entry_id)

    if request.method == 'GET':
        
        template = 'entries/detail.html'
        context = {
            'entry': entry
        }
        return render(request, template, context)


    elif ('delete' in form_data):
        entry.delete()

        entry_symptoms = SymptomEntry.objects.all()
        
        for entry_symptom in entry_symptoms:
            if (entry_symptom.id == entry_id): 
                entry_symptom.delete()
    
        return redirect('/entries')

        
