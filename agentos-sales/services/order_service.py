
from agentos_sales.models.order_model import Order
from uuid import uuid4

ORDERS: dict[str, Order] = {}

def create_order(data: Order)->Order:
    data.id = uuid4().hex
    ORDERS[data.id]=data
    return data

def list_orders():
    return list(ORDERS.values())

def calculate_commission(order: Order)->float:
    base = 0.05 if order.channel in ("site","insta") else 0.1
    return round(order.price*base,2)
