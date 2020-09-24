from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Medicine
import datetime

@login_required
def archived_medicines_list(request):
    if request.method == 'GET':
        todays_date = datetime.date.today().strftime("%Y-%m-%d") 
        medicines = Medicine.objects.filter(user=request.user).order_by('-end_date')
        pastMed = medicines.filter(end_date__lt=todays_date)
        context = {
            'medicines': pastMed,
        }

        return render(request, "medicines/archived.html", context)