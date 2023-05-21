from django import forms
from .models import BidderReg

class Regform(forms.ModelForm):
    class Meta:
        model = BidderReg
        fields = ['companyName','tinNo','companyRegNo','vatNo',
                  'location', 'region','dictrict','phone','email',
                  'website', 'business','category', 'foreignInput','employeeNum']