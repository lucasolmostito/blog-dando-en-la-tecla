from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import (
    View,
    CreateView,
    RedirectView
)

from django.views.generic.edit import (
    FormView,
    UpdateView
)

from .forms import (
    UserRegisterForm, 
    LoginForm,
    UpdatePasswordForm,
    UpdateInfoUserView
)
#
from .models import User
# 


class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('app_home:index')

    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            full_name=form.cleaned_data['full_name'],
            ocupation=form.cleaned_data['ocupation'],
            gender=form.cleaned_data['gender'],
            date_birth=form.cleaned_data['date_birth'],
        )
        # enviar el codigo al email del user
        return super(UserRegisterView, self).form_valid(form)



class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('app_home:index')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'app_home:index'
            )
        )


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('app_home:index')
    login_url = reverse_lazy('app_home:index')

    def form_valid(self, form):
        user = self.request.user
        new_password = form.cleaned_data['password2']
        user.set_password(new_password)
        user.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)
    

class UpdateInfoUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/update-info.html'
    form_class = UpdateInfoUserView
    success_url = reverse_lazy('app_favorites:perfil')
    login_url = reverse_lazy('app_home:index')
    
