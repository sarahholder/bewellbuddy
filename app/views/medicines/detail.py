from django.shortcuts import render 
from app.models import Medicine

def medicine_detail(request, medicine_id):
    if request.method == 'GET':
        medicine = Medicine.objects.get(pk=medicine_id)
        context = {
            'medicine': medicine
        }

        return render(request, "medicines/detail.html", context)