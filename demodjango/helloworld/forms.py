from django import forms
from django.forms import ModelForm
from .models import bill

class  billform(forms.ModelForm):
    class Meta:
        model = bill
        fields = ['customer_name', 'products']