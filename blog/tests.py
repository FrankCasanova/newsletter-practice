from django.http import response
from django.test import TestCase
# import user model, we need it to create users
from django.contrib.auth import get_user_model
# we also need import our path, in order to do that we need Reverse method
from django.urls import reverse
# import our Post model as well
from .models import Post

# Create your tests here.


class BlogTest(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create(
            username='testuser',
            email='test@email.com',
            password='1qaz3edc5tgb'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user
        )

    def test_string_representation(self):

        post = Post(title='a sample title')

        self.assertEqual(str(post), post.title)

    def test_post_content(self):

        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.body}', 'Nice body content')
        self.assertEqual(f'{self.post.author}', 'testuser')

    def test_post_list_view(self):

        # like if the client click on home
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):

        response = self.client.get('post_detail', '1')
        no_response = self.client.get('/post/456/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail')
