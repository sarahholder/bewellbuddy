from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import Entry, SymptomEntry
from django.contrib.auth.decorators import login_required

@login_required
def entries_list(request):
    form_data = request.POST

    if request.method == 'GET':
            
        entries = Entry.objects.filter(user=request.user).order_by('-entry_date')
        context = {
            "entries": entries
        }

        return render(request, "entries/list.html", context)

    elif request.method == 'POST':
        
        checked_symptoms = request.POST.getlist('symptoms')

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

        return redirect('/entries')