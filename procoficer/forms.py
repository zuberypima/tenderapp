from django import forms
from .models import ClientDetail

class Regform(forms.ModelForm):
    class Meta:
        model = ClientDetail
        fields =['idNo','orgName','orgCategory']