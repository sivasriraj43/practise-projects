# views.py
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        # Manually extract data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone_number = request.POST.get('phone_number', '')  # Optional, default to empty string
        address = request.POST.get('address', '')  # Optional, default to empty string

        # Option 1: Use a form for validation and saving
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')

        # Option 2: Manually validate and save (if not using a form)
        if name and email and message:  # Simple validation example
            contact = Contact(
                name=name,
                email=email,
                message=message,
                phone_number=phone_number,
                address=address,
            )
            contact.save()
            return redirect('success')

        # Handle invalid form or validation errors
        return render(request, 'contact_form.html', {'form': form, 'error': 'Invalid data'})
    
    else:
        # If GET request, render the form
        form = ContactForm()
    
    return render(request, 'contact_form.html', {'form': form})
