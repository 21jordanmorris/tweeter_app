from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Tweet

class TweetTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='specialpwd'
        )

        self.tweet = Tweet.objects.create(
            body='Nice tweet!',
            user=self.user,
        )

    def test_tweet_string(self):
        tweet = Tweet(body='A sample tweet')
        self.assertEqual(str(tweet), tweet.body)

    def test_tweet_content(self):
        self.assertEqual(f'{self.tweet.user}', 'testuser')
        self.assertEqual(f'{self.tweet.body}', 'Nice tweet!')

    def test_tweet_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice tweet!')
        self.assertTemplateUsed(response, 'home.html')

    def test_tweet_create_view(self):
        self.client.force_login(self.user) # new
        response = self.client.post(reverse('tweet_new'),
            {'body': 'New tweet'}, follow=True) # updated
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New tweet')