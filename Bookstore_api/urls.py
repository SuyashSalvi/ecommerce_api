from django.urls import path
from Bookstore_api.views import BookListView, BookDetailView, booksview, booksdetailview, add_to_cart, cart_view, remove_from_cart, checkout, remove_from_cart_by_cart, clear_cart

urlpatterns = [
    path('books_raw/', BookListView.as_view(), name='book-list'),
    path('books/', booksview, name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/?search=<str:pk>/', booksdetailview, name='book-detail'),
    path('cart/', cart_view, name='cart_view'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('remove-from-cart-by-cart/<int:book_id>/', remove_from_cart_by_cart, name='remove_from_cart_by_cart'),
    path('checkout/', checkout, name='checkout'),
    path('clear-cart/', clear_cart, name='clear_cart'),
]

