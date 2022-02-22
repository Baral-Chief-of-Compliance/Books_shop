from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import Book
from cart.forms import CartAddBookForm

def index(request):
    return render(request, 'Books_Shop_Site/index.html')


class BookClassView(ListView):
    models = Book
    queryset = Book.objects.all()
    template_name = "Books_Shop_Site/book_list.html"


class BookClassDetails(DetailView):
    model = Book
    cart_book_form = CartAddBookForm()
    template_name = "Books_Shop_Site/book_detail.html"
