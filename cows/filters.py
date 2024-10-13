import django_filters
from .models import Cow


class CowFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    department = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Cow
        fields = ['name', 'color', 'breed', 'features']
