from django.db import models
from users.models import User  # seller ke liye

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'seller'})
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
