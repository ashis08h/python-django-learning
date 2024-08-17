from django.db import models


class Blog(models.Model):
    DRAFT = 'draft'
    PUBLISH = 'publish'
    STATUS_CHOICES = [(DRAFT, 'draft'),
                      (PUBLISH, 'publish')]

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DRAFT)

    def __str__(self):
        return self.title


from rest_framework import serializers
from .models import Blog, Comment

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    blogs = BlogSerializers(many=True, read_only=True)

    class Meta:
        model=Comment
        fields = '__all__'


from rest_framework import viewsets
from .models import Blog, Comment
from .serializers import CommentSerializer, BlogSerializers


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


from django.urls import path, include
