from applications.home.models import Home
from applications.home.forms import ContactForm

# Proceso para recuparar teléfono y correo del registro home

def home_contact(request):
    home = Home.objects.latest('created')
    
    return {
        'phone': home.phone,
        'correo': home.contact_email,
        'contact_form': ContactForm,
    }