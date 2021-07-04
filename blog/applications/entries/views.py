from django.http import Http404, HttpResponseRedirect
from typing import List
from django.shortcuts import render
from django.views.generic import ListView, FormView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy, reverse

from .models import Category, Entry, Comments

from applications.users.forms import LoginForm


class EntryListView(ListView):
    template_name = 'entry/list.html'
    context_object_name = 'entries'
    paginate_by = 6
    success_url = reverse_lazy('app_home:index')
      
    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['form'] = LoginForm
        context['entry_favorites'] = Entry.objects.entries_user(self.request.user)
        return context
    
    
    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        category = self.request.GET.get('category', '')
        # Consulta para buscar
        result = Entry.objects.search_entry(kword, category)
        return result
    

class EntryDetailView(DetailView):
    template_name = 'entry/detail.html'
    model = Entry
    
    def get_context_data(self, **kwargs):
        
        current_entry = Entry.objects.get(slug=self.kwargs['slug'])
        
        context = super(EntryDetailView, self).get_context_data(**kwargs)
        context['form']= LoginForm
        context['categories']= Category.objects.all()
        context['comments']= Comments.objects.filter(entry=current_entry).order_by('-created')[:10]
        context['entry_favorites'] = Entry.objects.entries_user(self.request.user)

        return context

class AddCommentView(View):
    
    def post(self, request, *args, **kwargs):
        user = self.request.user
        current_entry = Entry.objects.get(slug=self.kwargs['slug'])
        comment = self.request.POST.get('comment')
        Comments.objects.add_comment(comment, user, current_entry)
        return HttpResponseRedirect(
            reverse(
                'app_entry:entry-detail',
                kwargs={"slug":self.kwargs['slug']}
            )
        )
