from django.http import JsonResponse
from django.shortcuts import render
from app.models import Symptom, SymptomEntry, Entry

def charts(request):

    return render(request, 'charts.html', {})

def get_data(request, *args, **kwargs):
    entries = Entry.objects.filter(user=request.user)
    symptoms = Symptom.objects.all()
    allSymptomEntries = SymptomEntry.objects.all()
    justMySymptomEntries = []

    for eachSymptomEntry in allSymptomEntries:
        for entry in entries: 
            if eachSymptomEntry.entry_id == entry.id:
                justMySymptomEntries.append(eachSymptomEntry)
                
    total = []
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    ten = []

    symptom_names = []
    symptom_colors = []

    for symptom in symptoms:
        symptom_names.append(symptom.name)
        symptom.color = ''.join('#'+ symptom.color)
        symptom_colors.append(symptom.color)

    for symptomEntry in justMySymptomEntries:
            if symptomEntry.symptom_id == 1:
                one.append(symptomEntry)
            if symptomEntry.symptom_id == 2:
                two.append(symptomEntry)
            if symptomEntry.symptom_id == 3:
                three.append(symptomEntry)
            if symptomEntry.symptom_id == 4:
                four.append(symptomEntry)
            if symptomEntry.symptom_id == 5:
                five.append(symptomEntry)
            if symptomEntry.symptom_id == 6:
                six.append(symptomEntry)
            if symptomEntry.symptom_id == 7:
                seven.append(symptomEntry)
            if symptomEntry.symptom_id == 8:
                eight.append(symptomEntry)
            if symptomEntry.symptom_id == 9:
                nine.append(symptomEntry)
            if symptomEntry.symptom_id == 10:
                ten.append(symptomEntry)
            
    thisList = [len(one), len(two), len(three), len(four), len(five), len(six), len(seven), len(eight), len(nine), len(ten)]
    print(thisList)
            
  
    default_items = [1, 4, 3, 5, 2, 6, 7, 9, 3, 2]
    data = {
        "labels": symptom_names, 
        "default": thisList,
        "colors": symptom_colors
    }
    return JsonResponse(data)

