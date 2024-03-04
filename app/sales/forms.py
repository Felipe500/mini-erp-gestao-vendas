from django import forms
from .models import ItemsSale, Sale
from app.products.models import Product, Category
from app.settings.models import MachineCard
from app.common.choices import FORMA_PG, STATUS_SALE
from app.customers.models import Customer


class ListMAqCartaoForm(forms.Form):
    maq_card = forms.ModelChoiceField(queryset=MachineCard.objects.all(), to_field_name='id', empty_label=None,
                                      required=True,
                                      label='Maquina de cartao', widget=forms.Select(
                                            attrs={"class": "passport",
                                                   'name': 'maq_list',
                                                   'onchange': "card_machines(this.value)"}
                                    ))


class ItemPedidoForm(forms.Form):
    categoria_list = forms.ModelChoiceField(queryset=Category.objects.all(),
                                            required=True,
                                            empty_label=None,
                                            label='CATEGORIA',
                                            widget=forms.Select(
                                                attrs={"class": "select form-control",
                                                       'name': 'produto_list',
                                                       'onchange': "products_by_category(this.value)"}
                                            ))
    produto_list = forms.ModelChoiceField(queryset=Product.objects.all(),
                                          empty_label=None,
                                          label='Produtos',
                                          required=False,
                                          widget=forms.Select(
                                            attrs={"class": "select form-control",
                                                   'name': 'cliente'}
                                        ))
    discount = forms.IntegerField(label='Desconto do Produto',
                                  initial=0,
                                  widget=forms.NumberInput(
                                        attrs={"class": "form-control",
                                               'name': 'desconto_produto',
                                               'id': 'id_desconto_produto'}))
    quantity = forms.IntegerField(label='Quantidade',
                                    initial=0,
                                    widget=forms.NumberInput(
                                        attrs={"class": "form-control",
                                               'name': 'quantidade',
                                               'id': 'id_quantidade'}))


class ItemForm(forms.ModelForm):
    discount = forms.DecimalField(label='Desconto',
                                  widget=forms.NumberInput(
                                      attrs={"class": "form-control",
                                             'name': 'desconto'}))

    class Meta:
        model = ItemsSale
        fields = ['quantity', 'discount']

        widgets = {

            'quantity': forms.NumberInput(attrs={"class": "form-control", 'name': 'cliente'}),
            'discount': forms.NumberInput(attrs={"class": "form-control", 'name': 'desconto',
                                                 'id':  'desconto_produto'})
        }


class ProdutoAddForm(forms.ModelForm):
    class Meta:
        model = ItemsSale
        fields = ['product']
        widgets = {
            'product': forms.Select(attrs={"class": "select form-control",
                                           'name': 'produto_list'}),
        }


class SaleForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Customer.objects.all(),
                                     required=True,
                                     label='Cliente',
                                     widget=forms.Select(
                                        attrs={"class": "select form-control"}
                                    ))
    discount = forms.IntegerField(
        label='Desconto',
        initial=0,
        widget=forms.NumberInput(
            attrs={"class": "form-control"}))

    def is_valid(self):
        result = super().is_valid()
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result

    class Meta:
        model = Sale
        fields = ['id', 'client', 'discount']

        widgets = {
            'cliente': forms.Select(attrs={"class": "form-control"})
        }


class VendaFormReadOnly(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Customer.objects.all(),
                                     required=True,
                                     label='Cliente',
                                     widget=forms.Select(
                                        attrs={"class": "select form-control", "readonly": True,
                                               "id": "id_cliente_readonly"}
                                    ))
    discount = forms.IntegerField(
        label='Desconto',
        initial=0,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "readonly": True}))

    def is_valid(self):
        result = super().is_valid()
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result

    class Meta:
        model = Sale
        fields = ['id', 'client', 'discount']


class FormPayment(forms.Form):
    set_payment_methods = forms.ChoiceField(label='Meios Pagamentos', required=False, initial=0, choices=FORMA_PG,
                                            widget=forms.Select(attrs={
                                                "class": "passport",
                                                'onchange': "payment_methods(this)"}
                                            ))
    pg_especie = forms.CharField(label='VALOR EM ESPECIE', required=False, initial=0,
                                 widget=forms.NumberInput(attrs={"class": "form-control amount",
                                                                 'oninput': "set_value(this)",
                                                                 'onscroll': "set_value(this)"}))
    pg_pix = forms.CharField(label='VALOR EM PIX', required=False, initial=0,
                             widget=forms.NumberInput(attrs={"class": "form-control amount",
                                                             'oninput': "set_value(this)",
                                                             'onscroll': "set_value(this)"}))
    pg_card = forms.CharField(label='VALOR EM CARTÃO', required=False, initial=0,
                              widget=forms.NumberInput(attrs={"class": "form-control amount",
                                                              'oninput': "set_value(this)",
                                                              'onscroll': "set_value(this)"}))
    taxas_maq = forms.CharField(label='Formas de pagamento:', required=True, initial=0,
                                widget=forms.Select(attrs={"class": "passport",
                                                           "name": "taxas_maq",
                                                           "id": 'taxas_maq'}))
