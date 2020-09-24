from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
import datetime
from app.models import Medicine

@login_required
def medicine_detail(request, medicine_id):
    form_data = request.POST
    todays_date = datetime.date.today().strftime("%Y-%m-%d")
    medicine = Medicine.objects.get(pk=medicine_id)

    if request.method == 'GET':
        template = 'medicines/detail.html'
        context = {
            'medicine': medicine
        }
        return render(request, template, context)


    elif request.method == 'POST':
        
        if ('put' in form_data):
            medicine.name = form_data['name']
            medicine.dosage = form_data['dosage']
            medicine.freqency = form_data['frequency']
            medicine.comments = form_data['comments']
            medicine.start_date = form_data['start_date']
            medicine.uploadImg = form_data['uploadImg']
            if form_data['end_date'] == '':
                medicine.end_date = None
            else:
                medicine.end_date = form_data['end_date']
            medicine.save()
            
            return redirect(reverse('app:medicine_detail', args=[medicine_id]))

        elif ('delete' in form_data and medicine.end_date != False):
            if medicine.end_date:
                medicine.delete()

                return redirect('/archived_medicine')
            else:
                medicine.delete()
                
            return redirect('/medicines')

    
    
    


        