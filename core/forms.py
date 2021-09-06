from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUsuario, Link


class CustomUsuarioCreateForm(UserCreationForm):
    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone', 'username')
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')


class LinkModelForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = ['nome', 'nickname', 'descricao', 'link', 'icone', 'imagem']

