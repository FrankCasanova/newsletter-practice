from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Post(models.Model):
    """
    A post model
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.user',
                               on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title
