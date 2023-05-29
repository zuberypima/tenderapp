from django.urls import path
from .views import homepage,procurementofficer,regClient,requireds

urlpatterns = [
    path('homepage',homepage,name='homepage'),
    path('procurementofficer',procurementofficer,name='procurementofficer'),
    path('regaclient', regClient,name='regaclient'),
    path('application',requireds, name='application'),
 
    # path('tenders',tenders,name='tenders')
]
  