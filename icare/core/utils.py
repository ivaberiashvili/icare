from django.db import transaction
# Make sure to import your Order and OrderItem models
from .models import Order, OrderItem

@transaction.atomic
def create_order_and_items(order_data, items_data):
    order = Order.objects.create(**order_data)
    for item in items_data:
        OrderItem.objects.create(order=order, **item)
    return order