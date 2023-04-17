from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.DO_NOTHING,related_name='user')
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    birth_date = models.DateField(null=True)

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=250)
    body = models.TextField(max_length=5000)
    author = models.ForeignKey(Author,related_name='post_author', on_delete=models.DO_NOTHING)