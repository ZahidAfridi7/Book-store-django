from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Book
# Create your views here.

def index(request):
    all_book = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        "all_books" : all_book
    })

def book_details(request,slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book-details.html",{
        "title": book.title,
        "author":book.author,
        "rating":book.rating,
        "is_bestSelling":book.is_bestSelling
    })    
    

    