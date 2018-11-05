from django.shortcuts import render

#create your views here

def default(request):
    return render(request, 'Registration/Registration_01.html')