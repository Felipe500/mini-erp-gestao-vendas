from datetime import date
import calendar
from django_filters import DateFilter

from django import forms

from .models import BillsReceive, BillsPay
from app.common import choices


def InicialDate():
    return date(year=date.today().year, month=date.today().month, day=1).strftime('%Y-%m-%d')


def FinalDate():
    days_month = calendar.monthrange(date.today().year, month=date.today().month)[1]
    return date(year=date.today().year, month=date.today().month, day=days_month).strftime('%Y-%m-%d')


class MovimentacoesFilter(forms.Form):
    tipo_entrada_filter = forms.ChoiceField(choices=choices.TIPO_MOVIMENTO_FILTER, label=('Tipo de Entrada'),
                                            widget=forms.Select(attrs={"class": "form-control mb-2 mr-sm-2",
                                                                       'onchange': "update_list_movements(1)"}))
    start_date_filter = forms.DateField(label=('Data Inicial'),
                                        initial=InicialDate(),
                                        widget=forms.DateInput(attrs={"class": "select form-control",
                                                                      'type': 'date',
                                                                      'onchange': "update_list_movements(1)"}))
    end_date_filter = forms.DateField(label=('Data Final'),
                                      initial=FinalDate(),
                                      widget=forms.DateInput(attrs={"class": "textinput textInput form-control",
                                                                    'type': 'date',
                                                                    'onchange': "update_list_movements(1)"}))


class CustomDateFilter(DateFilter):
    def filter(self, qs, value):
        if value:
            filter_lookups = {
                "%s__month" % (self.field_name,): value.month,
                "%s__year" % (self.field_name,): value.year
            }
            qs = qs.filter(**filter_lookups)
        return qs


class ContaReceberFilter(forms.Form):
    descricao_filter = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control mb-2 mr-sm-2",
                                                                'placeholder': 'Pesquisar',
                                                                "onkeyup": "update_list_to_receive(1)"}
                                                         )
                                  )
    categoria_filter = forms.ChoiceField(choices=choices.FILTER_CONTA_A_RECEBER, label=('Categoria'),
                                              widget=forms.Select(attrs={"class": "form-control mb-2 mr-sm-2",
                                                                         'placeholder': 'Categoria',
                                                                         'onchange': "update_list_to_receive(1)"}
                                                                       ))
    status_filter = forms.ChoiceField(choices=choices.FILTER_STATUS_PAYMENT_A_RECEBER, label=('Status'),
                                widget=forms.Select(attrs={"class": "form-control mb-2 mr-sm-2",
                                                           'placeholder': 'Status',
                                                           'onchange': "update_list_to_receive(1)"}))

    start_date_filter = forms.DateField(label=('Data Inicial'),
                                 widget=forms.DateInput(attrs={"class": "select form-control",
                                                               'type': 'date',
                                                               'onchange': "update_list_to_receive(1)"}))
    end_date_filter = forms.DateField(label=('Data Final'),
                          widget=forms.DateInput(attrs={"class": "textinput textInput form-control",
                                                        'type': 'date',
                                                        'onchange': "update_list_to_receive(1)"}))

    class Meta:
        model = BillsReceive
        fields = ['descricao_filter', 'categoria_filter', 'status', 'start_date', 'end_date']


class ContaPagarFilter(forms.Form):
    descricao_filter = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control mb-2 mr-sm-2",
                                                                'placeholder': 'Pesquisar',
                                                                "onkeyup": "update_list_bills_pay(1)"}
                                                         )
                                  )
    categoria_filter = forms.ChoiceField(choices=choices.FILTER_CONTA_A_PAGAR, label=('Categoria'),
                                              widget=forms.Select(attrs={"class": "form-control mb-2 mr-sm-2",
                                                                         'placeholder': 'Categoria',
                                                                         'onchange': "update_list_bills_pay(1)"}
                                                                       ))
    status_filter = forms.ChoiceField(choices=choices.FILTER_STATUS_PAYMENT_A_PAGAR, label=('Status'),
                                widget=forms.Select(attrs={"class": "form-control mb-2 mr-sm-2",
                                                           'placeholder': 'Status',
                                                           'onchange': "update_list_bills_pay(1)"}))

    start_date_filter = forms.DateField(label=('Data Inicial'),
                                 widget=forms.DateInput(attrs={"class": "select form-control",
                                                               'type': 'date',
                                                               'onchange': "update_list_bills_pay(1)"}))
    end_date_filter = forms.DateField(label=('Data Final'),
                          widget=forms.DateInput(attrs={"class": "textinput textInput form-control",
                                                        'type': 'date',
                                                        'onchange': "update_list_bills_pay(1)"}))

    class Meta:
        model = BillsPay
        fields = ['descricao_filter', 'categoria_filter', 'status', 'start_date', 'end_date']
