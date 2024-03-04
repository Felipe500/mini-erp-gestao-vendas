from .models import Customer
from django import forms
from datetime import datetime
from app.accounts.models.users import User


class ClienteForm(forms.ModelForm):
    name = forms.CharField(required=False,
                           label='Nome',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(required=False,
                                label='Sobrenome',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    birth_date = forms.DateField(label='Data de Nascimento',
                                 widget=forms.DateInput(attrs={'class': 'form-control'}, format='%d-%m-%y'),
                                 input_formats=['%Y-%m-%d'])

    phone = forms.CharField(required=False,
                              label='Celular',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=False,
                            label='Email',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}))
    zip = forms.CharField(required=False,
                          label='CEP',
                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=False,
                               label='Endereço',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    def is_valid(self):
        result = super().is_valid()
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result

    class Meta:
        model = Customer
        fields = '__all__'


class ClienteReadOnlyForm(forms.ModelForm):
    name = forms.CharField(required=False,
                           label='Nome',
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'readonly': 'readonly'}))
    surname = forms.CharField(required=False,
                                label='Sobrenome',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'readonly': 'readonly'}))

    birth_date = forms.DateField(initial=datetime.now().date(),
                                label='Data de Nascimento',
                                widget=forms.DateInput(attrs={'class': 'form-control',
                                                              'type': 'date',
                                                              'readonly': 'readonly'}))
    phone = forms.CharField(required=False,
                              label='Celular',
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'readonly': 'readonly'}))
    email = forms.CharField(required=False,
                            label='Email',
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'type': 'email',
                                                          'readonly': 'readonly'}))
    zip = forms.CharField(required=False,
                          label='CEP',
                          widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'readonly': 'readonly'}))
    address = forms.CharField(required=False,
                               label='Endereço',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'readonly': 'readonly'}))

    class Meta:
        model = Customer
        fields = '__all__'
