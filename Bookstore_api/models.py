from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

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

def get_default_user_id():
    user, created = User.objects.get_or_create(username='test')
    return user.id

class ShoppingCartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=get_default_user_id)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)