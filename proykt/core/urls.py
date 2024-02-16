from contact.views import contact_form_view
from core.views import home

from . import views     
from .views import contact
from django.urls import include, path

urlpatterns = [
    path("",home,name="home"),
    path('', views.index, name='index'),
    path('', views.about, name='about'),
    path('', include('contact.urls')),
    path('user/', include('user.urls')),
    path('contact/', contact_form_view, name='contact_form'),

]


