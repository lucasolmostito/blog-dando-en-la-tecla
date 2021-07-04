from django import forms
from django.contrib.auth import authenticate
from django.http import request
#
from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = (
            'email',
            'full_name',
            'ocupation',
            'gender',
            'date_birth',
        )
        
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ejemplo@ejemplo.com'
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre y Apellidos'
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ocupation': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Técnico, director, estudiante, etc...'
                }
            ),
            'date_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
        }
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Las contraseñas no son iguales, inténtalo de nuevo.')


class LoginForm(forms.Form):
    email = forms.CharField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo Electronico...',
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña...'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        return self.cleaned_data


class UpdatePasswordForm(forms.Form):

    email = forms.CharField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo Electronico...',
            }
        )
    )
    
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña Nueva'
            }
        )
    )
    password3 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Repite tu contraseña Nueva'

            }
        )
    )
    def clean(self):
        cleaned_data = super(UpdatePasswordForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        return self.cleaned_data
    
    def clean_password3(self):
        if self.cleaned_data['password3'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Las contraseñas no son iguales, inténtalo de nuevo.')
        

class UpdateInfoUserView(forms.ModelForm):
    
    class Meta:
        model = User
        fields = (
            'profile_picture',
            'full_name',
            'email',
            'ocupation',
            'gender',
            'date_birth',
        )
        
        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre y Apellidos',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ejemplo@ejemplo.com'
                }
            ),
            'ocupation': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Técnico, director, estudiante, etc...'
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'date_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
        }