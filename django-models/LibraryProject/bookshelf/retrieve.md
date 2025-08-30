# Retrieving Book Instances

```python
# Inside Django shell
from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(book)

# Expected Output:
# Book object (1)
```
