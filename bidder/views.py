from django.shortcuts import render,redirect
from .forms import Regform
# Create your views here.
def vendorreg(request):
    if request.method =='POST':
       form =Regform(request.POST)
       if form.is_valid():
           form.save()
           return redirect('success_page')
    else:
        form=Regform()
    return render(request, 'vendorregform.html',{'form':form})
