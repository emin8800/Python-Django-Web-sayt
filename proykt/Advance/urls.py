"""
URL configuration for Advance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from contact.views import contact_form_view, contact_success_view
from core.urls import urlpatterns as core_urls
from core.views import service,contact,about,room
from user.urls import urlpatterns as user_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(core_urls)),
    path("about.html", about, name='about'), 
    path('contact/', contact_form_view, name='contact_form'),
    path('contact/success/', contact_success_view, name='contact_success'),
    path("service.html", service, name='service'), 
    path("room.html",room,name='room'),
    path("user/", include(user_urlpatterns)),
    path('', include('contact.urls')),
    path('', include('store.urls')),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)