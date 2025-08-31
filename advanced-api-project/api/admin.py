# api/admin.py

from django.contrib import admin
from .models import Author, Book

# Register the Author model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year',)
    list_filter = ('author',)