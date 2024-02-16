# your_app/admin.py
from django.contrib import admin
from .models import *

admin.site.register(Setting)
admin.site.register(Edu)

