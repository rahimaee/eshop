from django.shortcuts import render
from eshop_contact.forms import ContactForm
from .models import Contact


# Create your views here.

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        message = contact_form.cleaned_data.get('message')
        Contact.objects.create(full_name=full_name, email=email, subject=subject, message=message)
        # todo : show user a success message
        contact_form = ContactForm()
    context = {
        'contact_form': contact_form,
    }
    return render(request, 'contact/contact_us_page.html', context)
