from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')

def skills(request):
    return render(request, 'skills.html')

def projects(request):
    return render(request, 'projects.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # (Optional) send email
            send_mail(
                subject=f"New message from {name}",
                message=f"From: {email}\n\nMessage:\n{message}",
                from_email='yourwebsite@gmail.com',
                recipient_list=['ndarathiofficial@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, "Thank you for reaching out! I’ll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})