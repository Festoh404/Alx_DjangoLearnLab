# Delete the book instance

```python
# Inside Django shell
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
print(Book.objects.all())

# Expected Output:
# <QuerySet []>
```
