from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from app.models import Medicine

@login_required
def medicine_detail(request, medicine_id):
    form_data = request.POST
    medicine = Medicine.objects.get(pk=medicine_id)

    if request.method == 'GET':
        context = {
            'medicine': medicine
        }

        return render(request, "medicines/detail.html", context)

    elif ('delete' in form_data and medicine.end_date != False):
        if medicine.end_date:
            medicine.delete()

            return redirect('/archived_medicine')
        else:
            medicine.delete()
            
            return redirect('/medicines')

    
    
    


        