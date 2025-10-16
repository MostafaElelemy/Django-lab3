from django.shortcuts import render, get_object_or_404
from .models import Book, Author

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    try:
        book = get_object_or_404(Book, id=book_id)
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})
    return render(request, 'book_detail.html', {'book': book})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'author_detail.html', {'author': author})
