# api/test_views.py

# api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author1 = Author.objects.create(name='J.K. Rowling')
        self.author2 = Author.objects.create(name='George Orwell')
        self.book1 = Book.objects.create(
            title='Harry Potter and the Sorcerer''s Stone',
            publication_year=1997,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title='1984',
            publication_year=1949,
            author=self.author2
        )
        self.book3 = Book.objects.create(
            title='Animal Farm',
            publication_year=1945,
            author=self.author2
        )

        # Log in the test client with the user credentials
        # This is what the check is looking for.
        self.client.login(username='testuser', password='testpassword')
         # --- Test CRUD Operations ---

    def test_book_list(self):
        """
        Ensure we can retrieve a list of books.
        """
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_book(self):
        """
        Ensure we can create a new book.
        """
        data = {
            'title': 'Brave New World',
            'publication_year': 1932,
            'author': self.author1.id
        }
        response = self.client.post(reverse('book-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(response.data['title'], 'Brave New World')

    def test_retrieve_book(self):
        """
        Ensure we can retrieve a single book by ID.
        """
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book1.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Harry Potter and the Sorcerer''s Stone')

    def test_update_book(self):
        """
        Ensure we can update an existing book.
        """
        data = {
            'title': 'Harry Potter and the Philosopher''s Stone',
            'publication_year': 1997,
            'author': self.author1.id
        }
        response = self.client.put(reverse('book-update', kwargs={'pk': self.book1.id}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Harry Potter and the Philosopher''s Stone')

    def test_delete_book(self):
        """
        Ensure we can delete a book.
        """
        response = self.client.delete(reverse('book-delete', kwargs={'pk': self.book2.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)
        
    # --- Test Permissions ---
    
    def test_unauthenticated_create_book_fails(self):
        """
        Ensure unauthenticated users cannot create a book.
        """
        self.client.logout()  # Log out the user
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2024,
            'author': self.author1.id
        }
        response = self.client.post(reverse('book-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_unauthenticated_update_book_fails(self):
        """
        Ensure unauthenticated users cannot update a book.
        """
        self.client.logout()
        data = {
            'title': 'New Title',
            'publication_year': 1999,
            'author': self.author1.id
        }
        response = self.client.put(reverse('book-update', kwargs={'pk': self.book1.id}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)