import django_filters
from .models import Staff
from django import forms


class StaffFilter(django_filters.FilterSet):
    lastname = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'filter-field'}))

    class Meta:
        model = Staff
        fields = ['lastname']
