from django.db import transaction
from django.db import connection
from .models import Order, OrderItem



@transaction.atomic
def create_order_and_items(order_data, items_data):
    order = Order.objects.create(**order_data)
    for item in items_data:
        OrderItem.objects.create(order=order, **item)
    return order


def get_price_ranked_products():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, name, price,
                   RANK() OVER (ORDER BY price ASC) AS price_rank
            FROM core_product
        """)
        return cursor.fetchall()