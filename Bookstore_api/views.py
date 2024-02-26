from django.shortcuts import render, redirect, get_object_or_404
from Bookstore_api.models import Book, ShoppingCartItem
from Bookstore_api.serializers import BookSerializer
from rest_framework import generics
from django.contrib.auth.decorators import login_required

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



@login_required
def booksview(request):
    search_query = request.GET.get('search',"")
    sort_order = request.GET.get('order',"asc")
    if  search_query:
        booklist=Book.objects.filter(title__icontains=search_query)
    else:
        if sort_order == "asc":
            booklist = Book.objects.all().order_by('title')
        elif sort_order == "desc":
            booklist = Book.objects.all().order_by('-title')
        else:
            # Handle other cases or set a default sorting order
            booklist = Book.objects.all().order_by('title')
    
    # return  render(request, 'Bookstore_api/list.html', {'books':Book.objects.all().order_by('title')})
    return  render(request, 'Bookstore_api/list.html', {'books':booklist})

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def booksdetailview(request, title):
    return  render(request, 'Bookstore_api/detail.html', {'books':Book.objects.all().order_by('title')})


@login_required
def add_to_cart(request, book_id):
    book = Book.objects.get(pk=book_id)
    user = request.user
    cart_item, created = ShoppingCartItem.objects.get_or_create(user=user, book=book)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('book-list')

@login_required
def cart_view(request):
    user = request.user
    cart_items = ShoppingCartItem.objects.filter(user=user)
    
    return render(request, 'Bookstore_api/cart.html', {'cart_items': cart_items})

@login_required
def remove_from_cart(request, cart_item_id):
    user = request.user
    cart_item = get_object_or_404(ShoppingCartItem, user=user, pk=cart_item_id)
    if cart_item.quantity>1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_view')

@login_required
def remove_from_cart_by_cart(request, book_id):
    user = request.user
    book_item = get_object_or_404(Book, id=book_id)
    cart_item = get_object_or_404(ShoppingCartItem, user=user, book=book_item)
    cart_item.delete()
    return redirect('cart_view')

@login_required
def checkout(request):
    user = request.user
    cart_items = ShoppingCartItem.objects.filter(user=user)

    total_quantity = sum(cart_item.quantity for cart_item in cart_items)
    total_price = sum(cart_item.book.price for cart_item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_quantity': total_quantity,
        'total_price': total_price,
    }

    # Clear the cart after retrieving information
    # ShoppingCartItem.objects.all().delete()

    return render(request, 'Bookstore_api/checkout.html', context)

@login_required
def clear_cart(request):
    user = request.user
    ShoppingCartItem.objects.filter(user=user).delete()
    return redirect('cart_view')