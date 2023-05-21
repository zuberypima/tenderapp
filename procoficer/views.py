from django.shortcuts import render
from django.http import HttpResponse
from .models import ClientDetail 
# Create your views here.

def homepage(request):
    return render(request, 'index.html')



def tenders(request):
    return render(request, 'viewtender.html')