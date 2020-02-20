# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin # new

class SignUpView(SuccessMessageMixin, generic.CreateView): # new
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    success_message = 'Account was created successfully.' # new

class UserUpdateView(SuccessMessageMixin, generic.UpdateView): # new
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'update.html'
    success_message = 'User profile updated.' # new

    # This keeps users from accessing the profile of other users.
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(id=user.id)

class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView): # new
    success_url = reverse_lazy('home')
    template_name = 'change_password.html'
    success_message = 'Password changed.' # new

class UserPasswordResetView(SuccessMessageMixin, PasswordResetView): # new
    success_url = reverse_lazy('login')
    template_name = 'reset_password.html'
    success_message = 'Check your email for a reset link.' # new
