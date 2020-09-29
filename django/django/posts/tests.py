from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text='a post')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'a post')


class PostViewPageTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text='another post')

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post.html')
