from django import forms
from .models import Staff


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['lastname', 'firstname', 'patronymic', 'post', 'works']
        widgets = {
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'post': forms.TextInput(attrs={'class': 'form-control'}),
            'works': forms.CheckboxInput(attrs={'class': 'form-check form-switch form-check-input'}),
        }
