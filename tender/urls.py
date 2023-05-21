from django.urls import path
from .views import tenders_list,tenderreg

urlpatterns = [
    path('tenders',tenders_list,name='tenders'),
    path('tenderreg',tenderreg,name='tenderreg')
]
  