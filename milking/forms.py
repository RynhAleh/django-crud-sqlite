from django import forms
from .models import Milking


class MilkingForm(forms.ModelForm):
    class Meta:
        model = Milking
        fields = ['datetime', 'staff_id', 'milk_amount_total', 'cows_milked', 'milk_amount_e',
                  'milk_amount_v', 'milk_amount_1', 'milk_fat_per', 'milk_prot_per']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'staff_id': forms.TextInput(attrs={'class': 'form-control'}),
            'milk_amount_total': forms.TextInput(attrs={'class': 'form-control'}),
            'cows_milked': forms.NumberInput(attrs={'class': 'form-control'}),
            'milk_amount_e': forms.TextInput(attrs={'class': 'form-control'}),
            'milk_amount_v': forms.TextInput(attrs={'class': 'form-control'}),
            'milk_amount_1': forms.TextInput(attrs={'class': 'form-control'}),
            'milk_fat_per': forms.TextInput(attrs={'class': 'form-control'}),
            'milk_prot_per': forms.TextInput(attrs={'class': 'form-control'}),
        }
