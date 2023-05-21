from django.urls import path
from .views import vendorreg

urlpatterns = [
    path('vendorreg',vendorreg, name='vendorreg')
]
