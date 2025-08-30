from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Library, Book
from django.contrib.auth.decorators import user_passes_test

def list_books(request):
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
    

from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in right after registration
            return redirect("book_list")  # redirect to your existing book list view
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Login view (using Django’s built-in AuthenticationForm)
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"
    authentication_form = AuthenticationForm

class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

