from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from app.models import Entry, SymptomEntry

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


    elif request.method == 'POST':

        entry_symptoms = SymptomEntry.objects.filter(entry=entry)

        if ('put' in form_data): 
            
            checked_symptoms = request.POST.getlist('symptoms')
            entry.entry_date = form_data['entry_date']
            entry.comments = form_data['comments']
            entry.save()
            
            for entry_symptom in entry_symptoms:
                entry_symptom.delete()

            for symptom in checked_symptoms:
                SymptomEntry.objects.create(
                entry = entry,
                symptom_id = symptom
            )
            
            return redirect(reverse('app:entriesdetail', args=[entry_id]))

        elif ('delete' in form_data):
            entry.delete()
        
            return redirect('/entries')
            
