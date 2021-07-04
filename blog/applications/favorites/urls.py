#
from django.urls import path
from . import views

app_name = "app_favorites"

urlpatterns = [
    path(
        'perfil/', 
        views.UserPageListView.as_view(),
        name='perfil',
    ),       
    path(
        'add-entrada/<pk>', 
        views.AddFavoritesView.as_view(),
        name='add-favourite',
    ),       
    path(
        'delete-favourite/<pk>', 
        views.FavoritesDeleteView.as_view(),
        name='delete-favourite',
    ),       
]