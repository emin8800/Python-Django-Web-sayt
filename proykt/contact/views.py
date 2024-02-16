# contact/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage

def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})

def contact_success_view(request):
    return render(request, 'contact/contact_success.html')
