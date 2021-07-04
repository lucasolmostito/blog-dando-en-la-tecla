#
from django.urls import path
from . import views

app_name = "app_entry"

urlpatterns = [
    path(
        'entradas/', 
        views.EntryListView.as_view(),
        name='entry-list',
    ),    
    path(
        'entrada/<slug>/', 
        views.EntryDetailView.as_view(),
        name='entry-detail',
    ),    
    path(
        'entrada/<slug>/add-comment/', 
        views.AddCommentView.as_view(),
        name='add-comment',
    ),    
]