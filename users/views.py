from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from braces.views import SelectRelatedMixin

from . import forms

# User dashboard for comments
class Dashboard(LoginRequiredMixin, SelectRelatedMixin, generic.DetailView):
    model = User
    select_related = ('days',)
    template_name = 'users/dashboard.html'

    def get_object(self, queryset=None):
        return self.request.user

# Allows users to record their daily earnings
class Record(LoginRequiredMixin, SelectRelatedMixin, generic.DetailView):
    model = User
    select_related = ('days',)
    template_name = 'users/record.html'

    def get_object(self, queryset=None):
        return self.request.user

# Allows users to logout
class LogoutView(LoginRequiredMixin, generic.FormView):
    form_class = forms.LogoutForm
    template_name = 'users/logout.html'

    def form_valid(self, form):
        logout(self.request)
        return HttpResponseRedirect(reverse('home'))

# Allows users to sign up
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:dashboard')

