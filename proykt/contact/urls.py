# contact/urls.py
from django.urls import path
from .views import contact_form_view, contact_success_view

urlpatterns = [
    path('contact/', contact_form_view, name='contact_form'),
    path('contact/success/', contact_success_view, name='contact_success'),\
    
]
