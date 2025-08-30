from django.urls import path
from .views import list_books, LibraryDetailView, register_view, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path("register/", register_view, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
