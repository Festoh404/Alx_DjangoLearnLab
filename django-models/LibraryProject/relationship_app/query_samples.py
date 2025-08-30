from .models import Author, Book, Library, Librarian

def books_by_author(author_name):
    author = Author.objects.filter(name=author_name)
    return Book.objects.filter(author)

def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian