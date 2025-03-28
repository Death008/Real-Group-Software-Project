""""Defines views for about."""
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from registration.models import UserProfile
from .forms import ContactForm


def contact(request):
    """
    Handles the contact page.
    Displays a contact form and sends an email with the submitted details if the form is valid.
    """
    form = ContactForm()
    
    if request.user.is_anonymous:
        userprofile = None
    else:
        userprofile = UserProfile.objects.get(user=request.user)
        

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # retrieves data from the contact form
            name = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
           
        
            html_content = render_to_string(
                "email/contact_email.html", {
                'name': name,
                'email': email,
                'message': message,
                }
            )
            # contructs email and sends using noreply email to customer service email
            email = EmailMessage(
                subject="Contact Form Submission",
                body=html_content,
                from_email="ecoquest.noreply@gmail.com",
                to=["ecoquest.customer.service@outlook.com"],
            )

            email.content_subtype = "html"
            email.send()

            return redirect("./")

    # variables passed into form
    context = {
        'forms':form,
        'user_auth': request.user,
        'userprofile': userprofile,
    }

    return render(request, 'contact.html', context)