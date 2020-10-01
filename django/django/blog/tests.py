from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='supersecretpassword',
        )

        self.post = Post.objects.create(
            title='A dummy post',
            body='A dummy content',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='A dummy post')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A dummy post')
        self.assertEqual(f'{self.post.body}', 'A dummy content')
        self.assertEqual(f'{self.post.author}', 'testuser')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A dummy content')
        self.assertTemplateUsed(response, 'home.html')

    def post_detail_view(self):
        response = self.client.get('/post/1')
        no_response = self.client.get('/post/1000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A dummy post')
        self.assertTemplateUsed(response, 'post_detail.html')
