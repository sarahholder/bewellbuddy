from django.shortcuts import render, redirect, reverse 
from django.contrib.auth.decorators import login_required
from app.models import Medicine
import datetime

@login_required
def medicines_list(request):
    if request.method == 'GET':
        todays_date = datetime.date.today().strftime("%Y-%m-%d")
        medicines = Medicine.objects.filter(user=request.user).order_by('-start_date')
        activeMed = medicines.exclude(end_date__lt=datetime.date.today())

        print(activeMed)
        currentMeds = []
        context = {
            'medicines': activeMed,
        }
        return render(request, "medicines/list.html", context)

    elif request.method == 'POST':
        form_data = request.POST

        if not form_data['end_date']:
            new_medicine = Medicine.objects.create(
                user = request.user, 
                name = form_data['name'],
                dosage = form_data['dosage'],
                frequency = form_data['frequency'],
                comments = form_data['comments'],
                start_date = form_data['start_date'], 
                uploadImg = form_data['uploadImg']
            )
        else:
            new_medicine = Medicine.objects.create(
                user = request.user, 
                name = form_data['name'],
                dosage = form_data['dosage'],
                frequency = form_data['frequency'],
                comments = form_data['comments'],
                start_date = form_data['start_date'], 
                end_date = form_data['end_date'],
                uploadImg = form_data['uploadImg']
            )
        return redirect(reverse('app:medicines'))