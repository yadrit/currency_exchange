from celery import shared_task
from account.models import Contact
from django.core.mail import send_mail


@shared_task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@shared_task
def send_email_async(subject, message, email_from, recipient_list):
    # contact_obj = Contact.objects.get(id=contact)
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)
