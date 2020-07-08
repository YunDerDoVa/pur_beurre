from django import forms


from .models import Account


class RegisterForm(forms.Form):

    name = forms.CharField(label='Nom d\'utilisateur', max_length=127)
    email = forms.EmailField(label='Adresse email', max_length=127)
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Mot de passe',
        max_length=127
    )
    password_2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirmer mot de passe',
        max_length=127
    )


class LoginForm(forms.Form):

    email = forms.CharField(label='Adresse email', max_length=127)
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Mot de passe',
        max_length=127
    )


class EditAccountForm(forms.ModelForm):

#    password_check = forms.CharField(
#        label='Entrer le mot de passe pour valider',
#        max_length=127,
#        widget=forms.PasswordInput(),
#    )

    class Meta:
        model = Account

        fields = [
            'allow_datashare',
        ]
