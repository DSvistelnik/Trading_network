from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from network_links.models import Network


class NetworkForm(forms.ModelForm):
    """Создание ссылки на поставщика"""
    class Meta:
        model = Network
        fields = '__all__'
        widgets = {
            'provider': ForeignKeyRawIdWidget(Network._meta.get_field('provider').remote_field, admin.site),
        }
