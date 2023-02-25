from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
# Create your views here.


class UserRegistrationView(generic.CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('main')
    
def main_page(request):
    return render(request, 'main.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })

class PasswordChangeView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change_password.html'

    def get_success_url(self):
        return reverse_lazy('main')
