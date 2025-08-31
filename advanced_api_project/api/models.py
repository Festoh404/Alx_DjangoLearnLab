# api/models.py

from django.db import models

# This model represents an author with a name.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# This model represents a book, linking to an author.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books' # The 'related_name' is important for nested serializers
    )

    def __str__(self):
        return f"{self.title} by {self.author.name}"