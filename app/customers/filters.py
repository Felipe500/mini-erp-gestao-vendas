import django_filters
from django_filters import CharFilter
from .models import Customer
from django import forms


class ClienteFilter(django_filters.FilterSet):
    nome = CharFilter(field_name='name',
                      label='Nome',
                      lookup_expr='icontains',
                      widget=forms.TextInput(
                         attrs={"class": "form-control",
                                         'placeholder': 'Nome'}))
    sobrenome = CharFilter(field_name='surname',
                           lookup_expr='icontains',
                           label='Sobrenome',
                           widget=forms.TextInput(
                              attrs={"class": "form-control",
                                              'placeholder': 'Sobrenome'}))

    class Meta:
        model = Customer
        fields = ['nome', 'sobrenome']


