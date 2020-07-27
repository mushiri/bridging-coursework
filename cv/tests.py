from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Card

class CvTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', email='test@email.com', password='secret')
        self.card = Card.objects.create(title='A good title', body='Nice body content', author=self.user,)

    def test_string_representation(self):
        card = Card(title='A sample title')
        self.assertEqual(str(card), card.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.card.get_absolute_url(), '/cv/card/1/')

    def test_card_content(self):
        self.assertEqual(f'{self.card.title}', 'A good title')
        self.assertEqual(f'{self.card.author}', 'testuser')
        self.assertEqual(f'{self.card.body}', 'Nice body content')

    def test_card_list_view(self):
        response = self.client.get(reverse('card_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'cv/card_list.html')

    def test_card_detail_view(self):
        response = self.client.get('/cv/card/1/')
        no_response = self.client.get('/cv/card/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'cv/card_detail.html')

    def test_card_create_view(self):
        response = self.client.post(reverse('card_new'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user,
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_card_update_view(self):
        response = self.client.post(reverse('card_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })

        self.assertEqual(response.status_code, 302)

    def test_card_delete_view(self):
        response = self.client.post(
            reverse('card_delete', args='1'))

        self.assertEqual(response.status_code, 302)

