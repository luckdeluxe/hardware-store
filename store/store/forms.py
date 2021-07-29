from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                                min_length=4, max_length=20,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'username'
                                }))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'id': 'email',
                                 'placeholder': 'example@accesogaming.com'
                             }))
    password = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'id': 'password'
                                }))
    password_repeat = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'id': 'password_repeat'
                                }))

    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El usuario ya se encuentra en uso')

        return username

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El usuario ya se encuentra en uso')

        return email


    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password_repeat') != cleaned_data.get('password'):
            self.add_error('password_repeat', 'Password not match')
