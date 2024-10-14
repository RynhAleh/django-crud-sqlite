import django_filters
from .models import Cow
from django import forms


class CowFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    color = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    breed = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'filter-field'}))

    class Meta:
        model = Cow
        fields = ['name', 'color', 'breed']
