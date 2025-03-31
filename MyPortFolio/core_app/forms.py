from django import forms 
from .models import model_login

class login_form(forms.ModelForm):
    class Meta:
        model = model_login 
        fields = ['user_name', 'password']

        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter User Name'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Password'
            }),
        }
        