from django.shortcuts import render, redirect
from app.models import Entry, SymptomEntry

def entry_detail(request, entry_id):
    form_data = request.POST

    if request.method == 'GET':
        entry = Entry.objects.get(pk=entry_id)
        context = {
            'entry': entry
        }
        return render(request, "entries/detail.html", context)

    elif ('delete' in form_data):
        entry = Entry.objects.get(pk=entry_id)
        entry_symptom = SymptomEntry.objects.get(pk=entry_id)
        entry.delete()
    
        return redirect('/entries')

        
