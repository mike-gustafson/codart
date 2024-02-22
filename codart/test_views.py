# test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Profile, Dart

class TestViews(TestCase):
    def setUp(self):
        # Setting up test client
        self.client = Client()

        # Creating test user and profile
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

        # Creating a Dart instance
        self.dart = Dart.objects.create(user=self.user, title='Test Dart')
        self.dart_like_url = reverse('dart_like', kwargs={'pk': self.dart.pk})
        self.dart_dislike_url = reverse('dart_dislike', kwargs={'pk': self.dart.pk})
        self.delete_dart_url = reverse('delete_dart', kwargs={'pk': self.dart.pk})

        # URLs
        self.home_url = reverse('home')
        self.profile_list_url = reverse('profile_list')
        self.profile_url = reverse('profile', args=[self.user.pk])
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.register_url = reverse('register')
        self.edit_profile_url = reverse('edit_profile')
        self.delete_profile_url = reverse('delete_profile')

    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_profile_list_GET_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.profile_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_list.html')

    def test_profile_list_GET_unauthenticated(self):
        response = self.client.get(self.profile_list_url)
        self.assertRedirects(response, self.home_url)

    def test_profile_GET(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_login_user_POST(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, self.home_url)

    def test_logout_user_GET(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, self.home_url)

    def test_register_user_POST(self):
        user_count = User.objects.count()
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 't3st1ngp455w0rd',
            'password2': 't3st1ngp455w0rd',
            'first_name': 'New',
            'last_name': 'User'
        })
        self.assertEquals(User.objects.count(), user_count + 1)
        self.assertEqual(response.status_code, 302)

    def test_edit_profile_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.edit_profile_url, {'username': 'testuser', 'first_name': 'Dave'})
        self.assertRedirects(response, reverse('profile', args=[self.user.pk]))
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Dave')

    def test_dart_like(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.dart_like_url)
        self.assertEqual(response.status_code, 200)
        self.dart.refresh_from_db()
        self.assertEqual(self.dart.total_likes(), 1)

    def test_dart_dislike(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.dart_dislike_url)
        self.assertEqual(response.status_code, 200)
        self.dart.refresh_from_db()
        self.assertEqual(self.dart.total_dislikes(), 1)

    def test_delete_dart(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.delete_dart_url)
        self.assertRedirects(response, reverse('home'))
        dart_exists = Dart.objects.filter(pk=self.dart.pk).exists()
        self.assertFalse(dart_exists, "Dart should be deleted but still exists.")

    def test_delete_profile(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.delete_profile_url)
        self.assertRedirects(response, reverse('home'), status_code=302, target_status_code=200)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username='testuser')

    def test_fetch_news(self):
        response = self.client.get(reverse('fetch-news'))
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    TestCase.main()
