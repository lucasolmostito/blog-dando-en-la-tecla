
from django import forms
from django.forms import widgets

# model
from .models import Contact, Suscribers

class SuscribersForm(forms.ModelForm):
    
    class Meta:
        model = Suscribers
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo electrónico...',
                }
            )
        }
        

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'full_name',
            'email',
            'message',
        )
        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Díganos su nombre...'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo electrónico'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '¿En qué puedo ayudarle? Le responderé lo antes posible...'
                }
            ),
        }