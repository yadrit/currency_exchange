from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from account.models import User


def smoke(request):
    return HttpResponse('smoke')


class UserCreate(CreateView):
    model = User
    fields = ['username', 'email']
    template_name = 'registration/registration.html'
