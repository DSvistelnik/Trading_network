import django_filters.rest_framework
from network_links.models import Network


class CountryFilter(django_filters.rest_framework.FilterSet):
    """Добавлена возможность фильтрации объектов по определенной стране"""
    country = django_filters.CharFilter(field_name='contacts__country')

    class Meta:
        model = Network
        fields = ('country',)
