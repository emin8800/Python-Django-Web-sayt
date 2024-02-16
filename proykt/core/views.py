from django.http import HttpResponse

from django.shortcuts import render

from core.models import *




def home(request):
    context = {
        "name": "Django",
        "edus": Edu.objects.all(),
    }
    return render(request, "index.html", context=context)



# def home(request):
#      return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request, "contact/contact_form.html")

def service(request):
    return render(request,"service.html")

def room(request):
    return render(request,"room.html")

def index(request):
    return render(request, 'core/index.html')
