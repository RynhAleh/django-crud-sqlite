from django import forms
from .models import Cow


class CowForm(forms.ModelForm):
    class Meta:
        model = Cow
        fields = ['name', 'color', 'breed', 'features']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control'}),
            'features': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
