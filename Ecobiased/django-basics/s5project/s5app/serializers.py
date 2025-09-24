from rest_framework import serializers
from .models import Author, NoteBook


class AuthorSerializers(serializers.ModelSerializer):

    class Meta:

        model = Author
        fields = ['name']


class NotebookSerializers(serializers.ModelSerializer):

    class Meta:

        model = NoteBook
        fields = '__all__'

