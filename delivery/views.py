from rest_framework import viewsets

from common.viewsets import CreateListRetrieveViewSet
from .models import Food, Order
from .serializers import FoodSerializer, OrderCreateSerializer, OrderReadSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.order_by('-id')
    serializer_class = FoodSerializer


class OrderViewSet(CreateListRetrieveViewSet):
    queryset = Order.objects.prefetch_related(
        'order_items__food',
    ).order_by(
        '-id',
    )
    create_serializer_class = OrderCreateSerializer
    read_serializer_class = OrderReadSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return self.create_serializer_class
        return self.read_serializer_class
