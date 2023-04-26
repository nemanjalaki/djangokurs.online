from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.DO_NOTHING,related_name='user')
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    birth_date = models.DateField(null=True)


    def __str__(self):
        return f'{self.name} {self.surname}'

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=250)
    body = models.TextField(max_length=5000)
    author = models.ForeignKey(Author,related_name='post_author', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.body}'
    
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=100)
    author = models.ForeignKey(Author,related_name='comment_author', on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post,related_name='comment_post', on_delete=models.DO_NOTHING)

    # class Meta: 
        # unique_together = ('body', 'post',)

    def __str__(self):
        return f'{self.body}'