from django.shortcuts import render
from app.models import Medicine


def archived_medicines_list(request):
    if request.method == 'GET':
            
        medicines = Medicine.objects.all().order_by('-end_date')
        context = {
            'medicines': medicines,
        }

        return render(request, "medicines/archived.html", context)