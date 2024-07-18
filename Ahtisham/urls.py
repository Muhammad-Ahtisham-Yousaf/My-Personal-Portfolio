from django.urls import path
from .import views

urlpatterns = [
    path('Portfolio',views.Portfolio, name='Portfolio'),
    path('About_Me',views.About_Me, name='About_Me'),
    path('form_sub',views.form_sub, name='form_sub'),
    path('Clients_details', views.clients_details, name='clients_details')
]
