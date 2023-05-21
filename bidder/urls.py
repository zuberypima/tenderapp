from django.urls import path
from .views import vendorreg, vendorhome

urlpatterns = [
    path('vendorreg',vendorreg, name='vendorreg'),
    path('vendor',vendorhome, name='vendor')
]
