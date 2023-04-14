from rest_framework import serializers

from authentication.serializers import CustomerSerializer
from .models import Food, Order, OrderItem


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class OrderItemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order']


class OrderItemReadSerializer(serializers.ModelSerializer):
    food = FoodSerializer()

    class Meta:
        model = OrderItem
        exclude = ['order']


class OrderCreateSerializer(serializers.ModelSerializer):
    order_items = OrderItemWriteSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'delivery_address',
            'payment_method',
            'order_items',
        ]

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items', None)
        request = self.context.get('request')
        order = Order.objects.create(customer=request.user, **validated_data)
        for order_item_data in order_items_data:
            OrderItem.objects.create(order=order, **order_item_data)
        return order


class OrderReadSerializer(serializers.ModelSerializer):
    order_items = OrderItemReadSerializer(many=True)
    total_amount = serializers.ReadOnlyField()
    customer = CustomerSerializer()

    class Meta:
        model = Order
        exclude = ['foods']
