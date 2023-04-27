from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import Author, Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'author',
        ]
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Your post title...'
                }),
            'body': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'cols': 27,
                'rows': 10,
                'placeholder': 'Your post goes here...'
                })
        }

