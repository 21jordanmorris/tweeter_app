from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class UserTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='specialpwd'
        )
        self.credentials = {'username': 'testuser', 'password': 'specialpwd'}

    def test_user_login(self):
        response = self.client.post(reverse('login'), self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
        self.assertEqual(response.status_code, 200)

    def test_user_logout(self):
        response = self.client.post(reverse('logout'), follow=True)
        self.assertFalse(response.context['user'].is_active)
        self.assertEqual(response.status_code, 200)

    def test_user_signup(self):
        response = self.client.post(reverse('signup'),
            {'username': 'testuser2',
             'password1': 'specialpwd2',
             'password2': 'specialpwd2'
            }, follow=True)
        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.filter(username = 'testuser2')
        self.assertEqual(users.count(), 1)

    def test_user_update_profile(self):
        u = self.user
        self.client.force_login(u)
        response = self.client.post(reverse('update_user',
            kwargs={'pk': self.user.id}),
            {'username':u.username,'email':u.email,
            'first_name':'Test', 'last_name':'Name',
            'dob':'01/22/1995', 'location':'BEC'}, follow=True)
        self.assertEqual(response.status_code, 200)
        u.refresh_from_db()
        self.assertEqual(u.last_name, 'Name')

    def test_change_password_url(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('change_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='change_password.html')

    def test_reset_password_url(self):
        response = self.client.get(reverse('reset_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='reset_password.html')