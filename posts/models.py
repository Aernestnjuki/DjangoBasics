from django.db import models

# Create your models here.

"""
class Post:
    title: str
    author: str
    content: str
    image: file
"""

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='uploads', default='default.png')
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Post {self.title}'