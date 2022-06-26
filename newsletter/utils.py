from django.conf import settings
from .models import NewsLeterContact, NewsLetter
from django.db.models import Q
from django.template.loader import render_to_string
from django.core.mail import send_mail
from bs4 import BeautifulSoup
from django.contrib.sites.models import Site
import logging

logger = logging.getLogger(__name__)

def send_all_newsletters():
    print("Sending unsent newsletters")
    site = Site.objects.first()
    for newsletter in NewsLetter.objects.filter(sent=False, is_draft=False):
        send_email(newsletter=newsletter, site=site)
    print("Done sendng unsent newsletters")
    

def send_email(newsletter: NewsLetter, site:Site):
    """Send NewsLetter to the various contacts in the database"""
    print(f"sending {newsletter}")
    sent_to = []
    for recipient in NewsLeterContact.objects.filter(~Q(newsletters=newsletter), active=True):
        try:
            print(f"Sending email for {recipient} and newsletter {newsletter}")
            send_email_for_recipient(newsletter=newsletter, recipient=recipient, site=site)
            sent_to.append(recipient)
        except Exception as e:
            print(e)
    for recipient in sent_to:
        newsletter.sent_to.add(recipient)
    newsletter.sent = True
    newsletter.save()
    print(f"Done sending emails for newsletter: {newsletter}")


def send_email_for_recipient(newsletter: NewsLetter, recipient: NewsLeterContact, site:Site):
    """Send the newsletter to a specific recipient."""

    email = render_to_string(
        "newsletter/base.html",
        context={
            "newsletter": newsletter,
            "recipient": recipient,
            "host_name": site.domain.strip("/"),
        },
    )
    soup = BeautifulSoup(email, features="html.parser")

    send_mail(
        subject=newsletter.title,
        message=soup.get_text(),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[recipient.email],
        html_message=email,
    )
