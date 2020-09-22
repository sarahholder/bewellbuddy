from django.shortcuts import render
from app.models import Medicine


def medicines_list(request):
    if request.method == 'GET':
            
        medicines = Medicine.objects.all().order_by('-start_date')
        context = {
            'medicines': medicines,
        }

        return render(request, "medicines/list.html", context)