from django.conf import settings
from Books_Shop_Site.models import Book


class Cart(object):

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    # def __iter__(self):
    #
    #
    #     book_id = self.cart.keys()
    #     books = Book.objects.filter(id__in = book_id)
    #
    #     cart = self.cart.copy()
    #     for book in books:
    #         cart[str(book.id)]['book'] = book
    #
    #     for item in cart.values():
    #         item['price'] = item['price']
    #         item['total_price'] = item['price'] * item['']


    def add(self, book, quantity = 1, update_quantity = False):

        book_id = str(book.id)
        if book_id not in self.cart:
            self.cart[book_id] = {quantity}
