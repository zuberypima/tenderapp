from django.shortcuts import render,redirect
from .models import TenderReg
from .forms import TenderRegForm
# Create your views here.



def tenderreg(request):
    if request.method =='POST':
       form =TenderRegForm(request.POST)
       if form.is_valid():
           form.save()
        #    return redirect('success_page')
           print('Succsessfully')
    else:
        form=TenderRegForm()
    return render(request, 'tenderreg.html',{'form':form})


def tenders_list(request):
    tenders=TenderReg.objects.all()

    return render(request, 'alltenders.html',{'tenders':tenders})



def viewtender(request,pk):
    tender=TenderReg.objects.get(tenderid=pk)
    return render(request, 'viewtender.html',{'tender':tender})



def applytender(request):
    return render(request, 'application.html')
