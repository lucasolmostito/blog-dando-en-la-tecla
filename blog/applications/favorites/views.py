from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import LoginRequiredMixin
# 
from django.views.generic import ListView, View
from django.views.generic.edit import DeleteView
# 
from .models import Favorites
from applications.entries.models import Entry


class UserPageListView(LoginRequiredMixin, ListView):
    template_name = 'favorites/perfil.html'
    context_object_name = 'entries_user'
    login_url = reverse_lazy('app_home:index')
    
    def get_queryset(self):
        return Favorites.objects.entries_user(self.request.user)
    

class AddFavoritesView(LoginRequiredMixin, View):  
    login_url = reverse_lazy('app_home:index')

    
    def post(self, request, *args, **kwargs):
        # recuperar el usuario
        user = self.request.user
        entry = Entry.objects.get(id=self.kwargs['pk'])
        # registramos una entrada favorita
        Favorites.objects.create(
            user=user,
            entry=entry,    
        )
        return HttpResponseRedirect(
            reverse(
                'app_favorites:perfil'
            )           
        )
        

class FavoritesDeleteView(DeleteView):
    model = Favorites
    success_url = reverse_lazy('app_favorites:perfil')
