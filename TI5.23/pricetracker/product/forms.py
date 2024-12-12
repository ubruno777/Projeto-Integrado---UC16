from django import forms
from .models import PriceProd
 
class PriceProdForm(forms.ModelForm):
    class Meta:
        model = PriceProd
        fields = ['priceprod', 'dateverify']  # Campos que você quer exibir no formulário