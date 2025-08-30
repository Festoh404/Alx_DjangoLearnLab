# Django Admin Integration for Bookshelf App

## Register Book Model

In `bookshelf/admin.py`, register the `Book` model so it appears in the Django admin.

```python
from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("publication_year",)
    search_fields = ("title", "author")

admin.site.register(Book, BookAdmin)
```
