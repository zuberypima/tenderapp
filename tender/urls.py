from django.urls import path
from .views import tenders_list,tenderreg,viewtender,applytender

urlpatterns = [
    path('alltenders',tenders_list,name='alltenders'),
    path('tenderreg',tenderreg,name='tenderreg'),
    path ('viewtender/<str:pk>/',viewtender, name='viewtender'),
    path ('application',applytender, name='application')
]
  