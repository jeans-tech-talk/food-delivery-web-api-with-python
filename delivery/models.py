from django.contrib.auth.models import User
from django.db import models
from django.db.models import F, Sum

from delivery.choices import PaymentMethod


class Food(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    objects = models.Manager()


class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
            total_amount=Sum(
                F('order_items__quantity') * F('order_items__food__price')
            ),
        )


class Order(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
    )
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_address = models.TextField()
    payment_method = models.CharField(
        max_length=25,
        choices=PaymentMethod.choices,
    )
    foods = models.ManyToManyField(
        'delivery.Food',
        related_name='orders',
        through='delivery.OrderItem',
    )

    objects = OrderManager()


class OrderItem(models.Model):
    order = models.ForeignKey(
        'delivery.Order',
        on_delete=models.CASCADE,
        related_name='order_items',
    )
    food = models.ForeignKey(
        'delivery.Food',
        on_delete=models.CASCADE,
        related_name='order_items',
    )
    quantity = models.PositiveSmallIntegerField()

    objects = models.Manager()
