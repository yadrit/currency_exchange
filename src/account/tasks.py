from celery import shared_task
# from account.models import Contact
from django.core.mail import send_mail
from django.urls import reverse




@shared_task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@shared_task()
def send_email_async(subject, message, email_from, recipient_list):
    # contact_obj = Contact.objects.get(id=contact)
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)


@shared_task()
def send_activation_code_async(email_to, code):
    path = reverse('account:activate', args=(code, ))
    send_mail(
        'Your activation code',
        f'http://127.0.0.1:8001{path}',
        'ivganivgan@gmail.com',
        [email_to],
        fail_silently=False,
    )