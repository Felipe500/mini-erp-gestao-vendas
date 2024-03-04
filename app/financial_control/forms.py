from django import forms
from .models import BillsPay, BillsReceive
from app.common import choices


class ContaPagarForm(forms.ModelForm):
    description = forms.CharField(label='descricao',
                                widget=forms.TextInput(attrs={"class": "form-control",
                                                              'name': 'descricao'}))
    value = forms.CharField(label='Valor',
                            widget=forms.NumberInput(attrs={"class": "numberinput form-control",
                                                            'name': 'valor'
                                                            }))
    category = forms.ChoiceField(choices=choices.CONTA_A_PAGAR,
                                  label="Categoria",
                                  required=True,
                                  initial='',
                                  widget=forms.Select(
                                      attrs={"class": "form-control select",
                                             "name": "categoria"}))
    status = forms.ChoiceField(choices=choices.STATUS_PAYMENT_A_PAGAR,
                               label="Status",
                               required=True,
                               initial='not_received',
                               widget=forms.Select(
                                   attrs={"class": "form-control select",
                                          "name": "categoria"}))

    def is_valid(self):
        result = super().is_valid()
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result

    class Meta:
        model = BillsPay
        fields = '__all__'


class ContaReceberForm(forms.ModelForm):
    description = forms.CharField(label='descricao',
                                widget=forms.TextInput(attrs={"class": "form-control",
                                                              'name': 'descricao'}))
    value = forms.CharField(label='Valor',
                            widget=forms.NumberInput(attrs={"class": "numberinput form-control",
                                                            'name': 'valor'
                                                            }))
    category = forms.ChoiceField(choices=choices.CONTA_A_RECEBER,
                                  label="Categoria",
                                  required=True,
                                  initial='',
                                  widget=forms.Select(
                                      attrs={"class": "form-control select",
                                             "name": "categoria"}))
    status = forms.ChoiceField(choices=choices.STATUS_PAYMENT_A_RECEBER,
                               label="Status",
                               required=True,
                               initial='not_received',
                               widget=forms.Select(
                                   attrs={"class": "form-control select",
                                          "name": "categoria"}))

    def is_valid(self):
        result = super().is_valid()
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result

    class Meta:
        model = BillsReceive
        fields = '__all__'
