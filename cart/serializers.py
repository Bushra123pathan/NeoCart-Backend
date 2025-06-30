from rest_framework import serializers
from .models import CartItem
from products.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    price = serializers.ReadOnlyField(source='product.price')

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name', 'price', 'quantity', 'added_at']
        read_only_fields = ['product_name', 'price', 'added_at']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be at least 1.")
        return value

    def validate(self, data):
        user = self.context['request'].user
        product = data.get('product')
        if CartItem.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError("Product already exists in cart.")
        return data
