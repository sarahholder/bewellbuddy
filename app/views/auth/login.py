from django.shortcuts import render

def login(request):
    if request.method == 'GET':
        template = 'login.html'

        return render(request, template)