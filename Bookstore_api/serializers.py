from rest_framework import serializers
from Bookstore_api.models import Book, ShoppingCartItem

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = "__all__"