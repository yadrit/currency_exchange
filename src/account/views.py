from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from account.models import User, Contact
from account.tasks import send_email_async

from currency_exchange import settings


def smoke(request):
    return HttpResponse('smoke')


class UserCreate(CreateView):
    model = User
    fields = ['username', 'email']
    template_name = 'registration/registration.html'


class MyProfile(UpdateView):
    template_name = 'my_profile.html'
    queryset = User.objects.filter(is_active=True)
    fields = ('email', )
    success_url = reverse_lazy('index')


class ContactUs(CreateView):
    template_name = 'my_profile.html'
    queryset = Contact.objects.all()
    fields = ('email', 'title', 'body')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)

        message = form.cleaned_data.get('body')
        subject = form.cleaned_data.get('title')
        email_from = form.cleaned_data.get('email')
        # contact = Contact.objects.get_or_create(email=email_from)[0]
        recipient_list = [settings.EMAIL_HOST_USER, ]

        send_email_async.delay(subject, message, email_from, recipient_list)

        return response
