# In api_project/api/serializers.py

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author'] # Note: `publication_date` was not in the previous model, so we'll omit it for now.