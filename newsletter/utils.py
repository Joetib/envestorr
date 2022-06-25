from django.conf import settings
from .models import NewsLeterContact, NewsLetter
from django.db.models import Q
from django.template.loader import render_to_string
from django.core.mail import send_mail
from bs4 import BeautifulSoup
from django.contrib.sites.models import Site

n = NewsLetter.objects.first()


def send_email(newsletter: NewsLetter):
    sent_to = []
    for recipient in NewsLeterContact.objects.filter(~Q(newsletters=newsletter)):
        try:
            send_email_for_recipient(newsletter=newsletter, recipient=recipient)
            sent_to.append(recipient)
        except Exception as e:
            print(e)
    for recipient in sent_to:
        newsletter.sent_to.add(recipient)
    newsletter.save()


def send_email_for_recipient(newsletter: NewsLetter, recipient: NewsLeterContact):
    recipients = NewsLeterContact.objects.filter(~Q(newsletters=newsletter))
    print(recipients)

    site = Site.objects.first()

    email = render_to_string(
        "newsletter/base.html",
        context={
            "newsletter": newsletter,
            "recipient": recipient,
            "host_name": site.domain.strip("/"),
        },
    )
    soup = BeautifulSoup(email)

    send_mail(
        subject=newsletter.title,
        message=soup.get_text(),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[recipient.email],
        html_message=email,
    )
