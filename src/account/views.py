from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView, View
from account.models import User, Contact, ActivationCode
from account.tasks import send_email_async
from account.forms import SignUpForm

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
    success_url = "/"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.request.user.id)


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


class SignUpView(CreateView):
    template_name = 'signup.html'
    queryset = User.objects.all()
    # fields = ('email', 'title', 'body')
    success_url = reverse_lazy('index')
    form_class = SignUpForm


class Activate(View):
    def get(self, request, activation_code):
        ac = get_object_or_404(ActivationCode.objects.select_related('user'), code=activation_code)
        if ac.is_expired:
            raise Http404

        ac.is_activated = True
        ac.save(update_fields=['is_activated'])

        user = ac.user
        user.is_active = True
        user.save(update_fields=['is_active'])
        return redirect('index')

