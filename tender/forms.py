from django import forms
from .models import TenderReg

class TenderRegForm(forms.ModelForm):
     class Meta:
          model =TenderReg 
          fields =['tenderid','description', 'clinteId',
                   'deadLineDate','procure_method', 
                   'financial_value', 'category',]