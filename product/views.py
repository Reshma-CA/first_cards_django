from django.shortcuts import render
from django.http import HttpResponse
from . models import products

# Create your views here.

def home(request):
    product = products.objects.all()
    return render(request,'home.html',{'product':product})

def about(request):
    return HttpResponse("<h1> About Page </h1>")


