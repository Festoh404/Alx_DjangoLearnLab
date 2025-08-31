from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ("title", "author", "publication_year")

    # Add filters in the sidebar
    list_filter = ("publication_year",)

    # Enable search functionality
    search_fields = ("title", "author")

# Register the model with its custom admin
admin.site.register(Book, BookAdmin)