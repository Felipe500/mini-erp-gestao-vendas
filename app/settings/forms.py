from django import forms
from .models import MachineCard
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

User = get_user_model()


class SelectPermissions(forms.ModelMultipleChoiceField):
    def label_from_instance(self, permission):
        return "%s" % permission.name


class CreateGroupForm(forms.ModelForm):
    name = forms.RegexField(regex=r'^[\w.@+-]+$',
                            max_length=30,
                            label="Nome",
                            widget=forms.TextInput(attrs={'class': 'form-control'}),
                            error_messages={
                                'invalid': "This value may contain only letters, numbers and @/./+/-/_ characters."})

    permissions = SelectPermissions(
        label="Permissões",
        queryset=Permission.objects.filter(codename__icontains='app'),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Group
        fields = '__all__'


class CreateUserForm(forms.ModelForm):
    required_css_class = 'required'
    name = forms.RegexField(regex=r'^[\w.@+-]+$',
                            max_length=30,
                            label="Nome",
                            widget=forms.TextInput(attrs={'class': 'form-control'}),
                            error_messages={'invalid': "This value may contain only letters, numbers and @/./+/-/_ characters."})
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                       'autocomplete': 'off',
                                       'name': 'user_email'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': "new-password"}),
        label="Senha")
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': "new-password"}),
        label="Confirme a senha")

    access_group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                          required=True,
                                          label='Grupo de Acesso',
                                          widget=forms.Select(attrs={"class": "select form-control"}))

    def clean(self,  errors={}):
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError("Email já cadastrado! por favor digite outro email.")
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            print(self.cleaned_data)
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                errors['password2'] = "A confirmação da senha não confere!"
        if errors:
            raise forms.ValidationError(errors)
        return self.cleaned_data

    class Meta:
        model = User
        fields = ("email", "name", "password1", "password2")


class ChangeUserForm(forms.ModelForm):
    required_css_class = 'required'
    name = forms.RegexField(regex=r'^[\w.@+-]+$',
                            max_length=30,
                            label="Nome",
                            widget=forms.TextInput(attrs={'class': 'form-control'}),
                            error_messages={'invalid': "This value may contain only letters, numbers and @/./+/-/_ characters."})
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                       'autocomplete': 'off',
                                       'name': 'user_email'})
    )
    photo = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control',
                                                           'onchange': 'previewFile(this);'}))
    access_group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                          required=True,
                                          label='Grupo de Acesso',
                                          widget=forms.Select(
                                             attrs={"class": "select form-control"})
                                          )

    def clean(self,  errors={}):
        if errors:
            raise forms.ValidationError(errors)
        return self.cleaned_data

    class Meta:
        model = User
        fields = ("email", "name", "photo", "access_group")


class CustomUserChangeForm(forms.ModelForm):
    name = forms.CharField(label='Usuário',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Nome Completo'}))
    email = forms.CharField(label='Email',
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Email@gmai.com'}))
    photo = forms.ImageField(required=False,widget=forms.FileInput(attrs={'class': 'form-control',
                                                           'onchange': 'previewFile(this);'}))

    class Meta:
        model = User
        fields = ("email", "name", "photo")




class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label='Senha Atual',
                                   widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Senha Atual'}))
    new_password1 = forms.CharField(label='Nova senha',
                                    widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                      'placeholder': 'Nova senha'}))
    new_password2 = forms.CharField(label='Confirme Nova Senha',
                                    widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                      'placeholder': 'Confirme sua Nova senha'}))

    def is_valid(self):
        result = super().is_valid()
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class FormMaq_cartao(forms.ModelForm):
    class Meta:
        model = MachineCard
        fields = '__all__'


class FormMaq_cartao2(forms.ModelForm):

    name = forms.CharField(required=True,
                           label='Nome',
                           widget=forms.TextInput(
                                          attrs={"class": "select form-control",
                                                 'name': 'descontos_list'}
                                      ))
    deb = forms.DecimalField(label='Débito',
                          widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type':"number",
                                        'step' : "0.01"}
                           ))
    cre1 = forms.DecimalField(label='Crédito X1',
                           widget=forms.NumberInput(
                              attrs={"class": "form-control",
                                     'name': 'descontos_list',
                                     'type': "number",
                                     'step': "0.01"}
                          ))
    cre2 = forms.DecimalField(label='Crédito X2',
                           widget=forms.NumberInput(
                              attrs={"class": "form-control",
                                     'name': 'descontos_list',
                                     'type': "number",
                                     'step': "0.01"}
                          ))
    cre3 = forms.DecimalField(label='Crédito X3',
                           widget=forms.NumberInput(
                              attrs={"class": "form-control",
                                     'name': 'descontos_list',
                                     'type': "number",
                                     'step': "0.01"}
                          ))
    cre4 = forms.DecimalField(label='Crédito X4',
                           widget=forms.NumberInput(
                              attrs={"class": "form-control",
                                     'name': 'descontos_list',
                                     'type': "number",
                                     'step': "0.01"}
                          ))
    cre5 = forms.DecimalField(label='Crédito X5',
                           widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type': "number",
                                      'step': "0.01"}
                           ))
    cre6 = forms.DecimalField(label='Crédito X6',
                           widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type': "number",
                                      'step': "0.01"}
                           ))
    cre7 = forms.DecimalField(label='Crédito X7',
                           widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type': "number",
                                      'step': "0.01"}
                           ))
    cre8 = forms.DecimalField(label='Crédito X8',
                           widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type': "number",
                                      'step': "0.01"}
                           ))
    cre9 = forms.DecimalField(label='Crédito X9',
                           widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type': "number",
                                      'step': "0.01"}
                           ))
    cre10 = forms.DecimalField(label='Crédito X10',
                            widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type': "number",
                                      'step': "0.01"}
                           ))
    cre11 = forms.DecimalField(label='Crédito X11',
                            widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type': "number",
                                      'step': "0.01"}
                           ))
    cre12 = forms.DecimalField(label='Crédito X12',
                            widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type': "number",
                                      'step': "0.01"}
                           ))

    class Meta:
        model = MachineCard
        fields ='__all__'









