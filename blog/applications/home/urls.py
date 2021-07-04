#
from django.urls import path
from . import views

app_name = "app_home"

urlpatterns = [
    path(
        '', 
        views.HomePageView.as_view(),
        name='index',
    ),  
    path(
        'registrar-suscripcion', 
        views.SuscriberCreateView.as_view(),
        name='add-suscription',
    ),  
    path(
        'contacto/', 
        views.ContactCreateView.as_view(),
        name='add-contact',
    ),  
]