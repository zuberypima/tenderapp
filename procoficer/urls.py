from django.urls import path
from .views import homepage,procurementofficer

urlpatterns = [
    path('homepage',homepage,name='homepage'),
    path('procurementofficer',procurementofficer,name='procurementofficer')
    # path('tenders',tenders,name='tenders')
]
  