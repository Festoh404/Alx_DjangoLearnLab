from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

def book_list(request):
    """Display all books and their authors"""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view for Library Detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        """Add books for the library to the context."""
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
