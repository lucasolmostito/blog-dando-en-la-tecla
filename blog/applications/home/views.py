import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail


from django.views.generic import TemplateView, CreateView, FormView

# apps entry
from applications.entries.models import Entry, Category
from applications.users.forms import LoginForm


# modelos
from .models import Home
from applications.favorites.models import Favorites

# formulario
from .forms import ContactForm, SuscribersForm


class HomePageView(FormView):
    template_name = "home/index.html"
    form_class = LoginForm
    success_url = reverse_lazy('app_favorites:perfil')
    
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # cargamos el home
        context['home'] = Home.objects.latest('created')
        # contexto de portada
        context['cover'] = Entry.objects.cover_entry()
        # contexto para los artículos en home
        context['home_entry'] = Entry.objects.in_home_entry()
        # contexto para las entradas recientes
        context['recent_entry'] = Entry.objects.recent_entry()
        # contexto para categorias
        context['categories'] = Category.objects.all()
        # contexto para lista de favoritos
        context['entry_favorites'] = Entry.objects.entries_user(self.request.user)
            
        return context
    
    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
     
        return super(HomePageView, self).form_valid(form)
    


class SuscriberCreateView(CreateView):
    form_class = SuscribersForm
    success_url = '.'


class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('app_home:index')
    
    def form_valid(self, form):
        
        # Send email
        subject = form.cleaned_data['full_name'] + ' quiere contactar contigo desde el blog.'
        message = 'El usuario ' + form.cleaned_data['full_name'] + ' con correo electrónico ' + form.cleaned_data['email'] + ' te deja este mensaje: ' + form.cleaned_data['message']
        sender_email = 'lucasfernandoolmos@gmail.com'
        print(sender_email)
        send_mail(subject, message, sender_email, ['lucasfernandoolmos@gmail.com'])
        
        return super(ContactCreateView, self).form_valid(form)
