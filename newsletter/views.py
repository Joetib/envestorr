from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from newsletter.forms import NewsLetterContactForm
from .models import NewsLeterContact, NewsLetter
from .utils import send_email
# Create your views here.


def newsletter(request):
    newsletter = NewsLetter.objects.first()
    send_email(newsletter=newsletter)
    return render(request, "newsletter/base.html", {"newsletter": newsletter, "host_name": "http://localhost:8000"})


def subscribe(request: HttpRequest) -> HttpResponse:
    created: bool
    newsletter_contact: NewsLeterContact

    if request.method != "POST":
        raise Http404("Method not allowed")
    if request.method == "POST":
        newsletter_contact_form = NewsLetterContactForm(request.POST)
        if newsletter_contact_form.is_valid():
            data = newsletter_contact_form.cleaned_data
            email = data['email']
            first_name = data['first_name']
            last_name = data["last_name"]
            newsletter_contact, created = NewsLeterContact.objects.get_or_create(email=email)
            newsletter_contact.first_name = first_name
            newsletter_contact.last_name = last_name
            newsletter_contact.active = True
            newsletter_contact.save()
            if created:
                messages.success(request, "You have been successfully added to the mailing list.")
            else:
                messages.success(request, "Your subscription has been updated.")
        else:
            messages.error(request, "There was an error while subscribing.")
    return redirect("home")

