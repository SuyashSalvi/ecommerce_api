from django.db import models
from django.contrib.auth.models import User


# title, author, description, price, and availability.
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.BooleanField(default=True)
    
    # def __str__(self):
    #     book_detail = self.title+ " "+self.author+" "+ self.description
    #     return book_detail



class ShoppingCartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)