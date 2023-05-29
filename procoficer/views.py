from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ClientDetail ,Condition
from .forms import  Regform
# Create your views here.

def homepage(request):
    return render(request, 'index.html')



def tenders(request):
    return render(request, 'viewtender.html')





def procurementofficer(request):
    return render(request, 'procurementofficer.html')


def regClient(request):
    if request.method =='POST':
       form =Regform(request.POST)
       if form.is_valid():
           form.save()
        #    return redirect('success_page')
           print('Sucess')
    else:
        form=Regform()
    return render(request, 'regaclient.html',{'form':form})


def requireds(request):
    conditions = Condition.objects.all()
    return render(request,'application.html',{'conditions':conditions})