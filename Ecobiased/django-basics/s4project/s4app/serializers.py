from rest_framework import serializers
from .models import Author, NoteBook


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['name']


class NotebookSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoteBook
        fields = '__all__'