# tweets/views.py
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin #new
from .models import Tweet

class TweetListView(ListView):
    model = Tweet
    template_name = 'home.html'

class TweetCreateView(LoginRequiredMixin, CreateView): # new
    model = Tweet
    template_name = 'tweet_new.html'
    fields = ['body'] # removed user

    def get_success_url(self):
        return reverse('home')

    def get_login_url(self): # new
        return reverse('login') # new

    def form_valid(self, form): # new
        form.instance.user = self.request.user # new
        return super().form_valid(form) # new