from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price_at_order_time']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'status', 'created_at', 'items']
        read_only_fields = ['user', 'total_price', 'created_at', 'items']

    def validate(self, data):
        user = self.context['request'].user
        from cart.models import CartItem
        cart_items = CartItem.objects.filter(user=user)
        if not cart_items.exists():
            raise serializers.ValidationError("Cart is empty. Cannot place order.")
        return data
