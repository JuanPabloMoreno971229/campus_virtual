import email
from email import message
from pickle import TRUE
from django import forms
from usuario.models import User

class UserForm(forms.Form):
    
    user = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'type': 'text', 'name':'username', 'class': 'form-control form-control-user', 'id': 'InputUser', 'aria-describedby':'emailHelp', 'placeholder':'Ingresar usuario...'}
    ))
    password = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(
        attrs={'type':'password', 'name':'password', 'class':'form-control form-control-user', 'id':'InputPassword', 'placeholder':'Contraseña'}
    ))
    
    class Meta:
        model = User
        fields = '__all__'
        