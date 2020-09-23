from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Medicine

@login_required
def archived_medicines_list(request):
    if request.method == 'GET':
            
        medicines = Medicine.objects.filter(user=request.user).order_by('-end_date')
        context = {
            'medicines': medicines,
        }

        return render(request, "medicines/archived.html", context)