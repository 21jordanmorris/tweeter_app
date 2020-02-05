from django.urls import path
from .views import TweetListView, TweetCreateView

urlpatterns = [
    path('tweets/new/', TweetCreateView.as_view(), name='tweet_new'),
    path('', TweetListView.as_view(), name='home'),
]