from rest_framework import serializers
from s3app.models import Author, NoteBook


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['name']


class NoteBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoteBook
        fields = '__all__'