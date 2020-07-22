from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import App

class ApplicationsTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', email='test@email.com', password='secret')
        self.app = App.objects.create(
                                      title='Test title',
                                      body='Nice body content',
                                      image='img/applications/test.png',
                                      author=self.user,)

    def test_string_representation(self):
        app = App(body='A sample body')
        self.assertEqual(str(app), app.body)

    def test_get_absolute_url(self):
        self.assertEqual(self.app.get_absolute_url(), '/app/1/')

    def test_app_content(self):
        self.assertEqual(f'{self.app.title}', 'Test title')
        self.assertEqual(f'{self.app.author}', 'testuser')
        self.assertEqual(f'{self.app.body}', 'Nice body content')
        self.assertEqual(f'{self.app.image}', 'img/applications/test.png')

    def test_app_list_view(self):
        response = self.client.get(reverse('home_applications'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'img/applications/test.png')
        self.assertTemplateUsed(response, 'applications/home.html')

    def test_app_detail_view(self):
        response = self.client.get('/app/1/')
        no_response = self.client.get('/app/100000/')
        self.assertContains(response, 'Test title')
        self.assertContains(response, 'Nice body content')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'applications/app_detail.html')

    def test_app_create_view(self):
        response = self.client.post(reverse('app_new'), {
            'title': 'New title',
            'author': self.user,
            'body': 'New text',
            'image': 'img/applications/new.png',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')
        self.assertContains(response, 'img/applications/new.png')

    def test_app_update_view(self):
        response = self.client.post(reverse('app_edit', args='1'), {
            'title': 'Updated title',
            'author': self.user,
            'body': 'Updated text',
            'image': 'img/applications/updated.png',
        })

        self.assertEqual(response.status_code, 302)

    def test_app_delete_view(self):
        response = self.client.post(
            reverse('app_delete', args='1'))

        self.assertEqual(response.status_code, 302)