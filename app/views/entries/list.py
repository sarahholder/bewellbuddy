from django.shortcuts import render
from app.models import Entry, Symptom, SymptomEntry


def entries_list(request):
    entries = Entry.objects.all()
   

    # for symptomEntry in symptomEntries:
    #     for entry in entries:
    #         entry.symptoms = []
    #         if entry.id == symptomEntry.entry_id:
    #             for symptom in symptoms:
    #                 if symptom.id == symptomEntry.symptom_id:
    #                     entry.symptoms.append(symptom)
    
    #     print(symptomEntries)
    
    # print(entries[0].symptomentry_set.all()[1].symptom)
    context = {
        "entries": entries,
    }

    return render(request, "entries/list.html", context)