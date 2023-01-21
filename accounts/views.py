from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import (
    login as auth_login,
)

class SignupView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

class LoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        """Security check complete. Log the user in. PERFORM CUSTOM CODE."""
        auth_login(self.request, form.get_user())
        form.get_user().execute_after_login()  # Custom code
        return HttpResponseRedirect(self.get_success_url())
