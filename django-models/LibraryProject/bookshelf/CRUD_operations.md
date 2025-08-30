# CRUD Operations in Django Shell

This document demonstrates how to perform **Create, Read, Update, and Delete (CRUD)** operations on the Book model using the Django shell.

---

## Full CRUD Workflow

```python
# Import the model
from bookshelf.models import Book

# -----------------
# 1. CREATE
# -----------------
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Expected Output:
# <Book: Book object (1)>


# -----------------
# 2. READ
# -----------------
# Retrieve all books
Book.objects.all()
# Expected Output:
# <QuerySet [<Book: 1984>]>

# Retrieve a single book by title
book = Book.objects.get(title="1984")
print(book.title)
# Expected Output:
# "1984"


# -----------------
# 3. UPDATE
# -----------------
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
print(book.title)
# Expected Output:
# "Nineteen Eighty-Four"


# -----------------
# 4. DELETE
# -----------------
book.delete()

# Confirm deletion
Book.objects.all()
# Expected Output:
# <QuerySet []>
```
