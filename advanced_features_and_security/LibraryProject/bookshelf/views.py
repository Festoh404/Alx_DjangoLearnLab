from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.db.models import Q

@permission_required("relationship_app.can_view", raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/book_list.html", {"books": books})

@permission_required("relationship_app.can_create", raise_exception=True)
def add_book(request):
    # Logic for adding a book
    pass

@permission_required("relationship_app.can_edit", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Logic for editing a book
    pass

@permission_required("relationship_app.can_delete", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Logic for deleting a book
    pass

def book_list(request):
    """Secure search using Django ORM (prevents SQL injection)"""
    books = Book.objects.all()
    
    search_query = request.GET.get('q', '').strip()
    if search_query:
        # Safe query using Q objects
        books = books.filter(
            Q(title__icontains=search_query) |
            Q(author__icontains=search_query)
        )
    
    return render(request, 'bookshelf/book_list.html', {'books': books})

def get_book(request, book_id):
    """Safe object retrieval"""
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookshelf/book_detail.html', {'book': book})

