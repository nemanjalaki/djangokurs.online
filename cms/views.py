from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework import generics

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Author, Post, Comment
from .serializers import AuthorSerializer, PostSerializer, CommentSerializer


# Create your views here.
class AuthorViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer

    search_fields = ['name', 'surname']

class PostViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer

    search_fields = ['title', 'body']

class CommentViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Comment.objects.all().order_by('id')
    serializer_class = CommentSerializer

