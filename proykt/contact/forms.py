# contact/forms.py
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
  
    class Meta:
        model = ContactMessage
        fields ='__all__'





