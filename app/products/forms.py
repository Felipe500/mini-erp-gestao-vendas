from django import forms
from .models import Product, Stock, Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='Nome',
                           widget=forms.TextInput(attrs={"class": "form-control"}))

    def is_valid(self):
        result = super().is_valid()
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result

    class Meta:
        model = Category
        fields = ['name']


class ProductForm(forms.ModelForm):
    description = forms.CharField(label='descricao', required=False,
                                widget=forms.TextInput(attrs={"class": "form-control", 'name': 'descricao'}))
    price = forms.CharField(label='preco', required=False,
                            widget=forms.NumberInput(attrs={"class": "numberinput form-control",
                                                            'name': 'preco'
                                                            }))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                       empty_label=None,
                                       label='Categoria',
                                       widget=forms.Select(
                                       attrs={"class": "form-control select",
                                              "name": "categoria"}))

    def clean(self, errors={}):
        if not self.cleaned_data['description']:
            errors['description'] = "Este campo é obrigatório!"
        if not self.cleaned_data['price']:
            errors['price'] = "Este campo é obrigatório!"
        if errors:
            raise forms.ValidationError(errors)

        return super().clean()

    def is_valid(self):
        result = super().is_valid()
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result

    class Meta:
        model = Product
        fields = '__all__'


class NewProductForm(forms.ModelForm):
    description = forms.CharField(label='Descrição', required=False,
                                widget=forms.TextInput(attrs={"class": "form-control",
                                                              'name': 'descricao'}))
    price = forms.CharField(label='Preço', required=False,
                            widget=forms.NumberInput(attrs={"class": "numberinput form-control",
                                                            'name': 'preco'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                       empty_label=None,
                                       label='Categoria',
                                       widget=forms.Select(
                                       attrs={"class": "form-control select",
                                              "name": "categoria"}))
    current_stock = forms.CharField(label='Estoque Atual', required=True,
                                    widget=forms.NumberInput(attrs={"class": "numberinput form-control",
                                                                    'name': 'estoque'}))
    minimum_stock = forms.CharField(label='Estoque Minimo', required=True,
                                    widget=forms.NumberInput(attrs={"class": "numberinput form-control",
                                                                    'name': 'estoque'}))

    def clean(self, errors={}):
        if not self.cleaned_data['description']:
            errors['description'] = "Este campo é obrigatório!"
        if not self.cleaned_data['price']:
            errors['price'] = "Este campo é obrigatório!"
        if not self.cleaned_data['category']:
            errors['category'] = "Selecione uma categoria!"

        if errors:
            raise forms.ValidationError(errors)

        return super().clean()

    def is_valid(self):
        result = super().is_valid()
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result

    class Meta:
        model = Product
        fields = '__all__'


class ProductFormReadOnly(forms.ModelForm):
    description = forms.CharField(label='Descrição', required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'readonly': 'readonly'}))
    price = forms.CharField(label='Preço', required=False,
                            widget=forms.NumberInput(attrs={'class': 'form-control',
                                                              'readonly': 'readonly'}))

    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                       empty_label=None,
                                       label='Categoria',
                                       widget=forms.Select(
                                           attrs={'class': 'form-control',
                                                  'readonly': 'readonly'}))

    class Meta:
        model = Product
        fields = '__all__'


class StockForm(forms.ModelForm):
    current_stock = forms.CharField(label='Estoque atual', required=False,
                                    widget=forms.NumberInput(attrs={"class": "numberinput form-control"}))
    minimum_stock = forms.CharField(label='Estoque Minimo', required=False,
                                    widget=forms.NumberInput(attrs={"class": "numberinput form-control"}))

    def clean(self, errors={}):
        if not self.cleaned_data['current_stock']:
            errors['current_stock'] = "Este campo é obrigatório!"
        if not self.cleaned_data['minimum_stock']:
            errors['minimum_stock'] = "Este campo é obrigatório!"

        if errors:
            raise forms.ValidationError(errors)

        return super().clean()

    def is_valid(self):
        result = super().is_valid()
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result

    class Meta:
        model = Stock
        fields = ['current_stock', 'minimum_stock']


class AddStockForm(forms.Form):
    add_stock = forms.CharField(label='Nova Entrada', required=False, initial=0,
                                  widget=forms.NumberInput(attrs={"class": "numberinput form-control",
                                                                  'oninput': "calculator_new_stock(this)"}))

    def clean(self, errors={}):
        if int(self.cleaned_data['add_stock']) < 1:
            errors['add_stock'] = "Não permitido valor igual zero (0)!"
        if errors:
            raise forms.ValidationError(errors)
        return super().clean()


class OutputStockForm(forms.Form):
    output_stock = forms.CharField(label='Nova Saída', required=False, initial=0,
                                     widget=forms.NumberInput(attrs={"class": "numberinput form-control",
                                                                     'oninput': "calculator_new_stock(this, 'sub')"}))

    def clean(self, errors={}):
        if int(self.cleaned_data['output_stock']) < 1:
            errors['output_stock'] = "Não permitido valor igual zero (0)!"
        if errors:
            raise forms.ValidationError(errors)
        return super().clean()
