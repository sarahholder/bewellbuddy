from django.shortcuts import render
from app.models import SymptomEntry

def symptomEntries_list(request):
    entries = SymptomEntry.objects.all()
    context = {
        "entries": entries
    }

    return render(request, "symptomEntries/list.html", context)