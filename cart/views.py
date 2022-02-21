from django.shortcuts import render, redirect, get_object_or_404
from Books_Shop_Site.models import Book
from .cart import Cart
from .forms import CartAddBookForm
from django.views.decorators.http import require_POST
# Create your views here.


@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id = book_id)
    form = CartAddBookForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book = book, quantity=cd['quantity'], update_quantity=['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddBookForm(initial={'quantity': item['quantity'], 'update': True})

    return render(request, 'cart/detail.html',{'cart':cart})
