from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework import generics

from .models import Author, Post
from .serializers import AuthorSerializer, PostSerializer


# Create your views here.
class AuthorViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer

    search_fields = ['name', 'surname', 'language_name']
    
class PostViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer