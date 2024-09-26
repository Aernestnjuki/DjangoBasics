from django.test import TestCase
from .models import Post

# Create your tests here.

class PostTestCase(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title = 'Test Title',
            author = 'Test Author',
            content = 'Test Content'
        )


    def test_home_page(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'List of posts with pagination')

    def test_post_creation(self):

        post_to_test = Post.objects.get(id=1)

        post_title = f'{post_to_test.title}'

        self.assertEqual(self.post.title, post_title)
        self.assertEqual(self.post.title, 'Test Title')
        self.assertEqual(self.post.author, 'Test Author')