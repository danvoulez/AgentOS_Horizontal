
from agentos_sales.models.order_model import Order
from agentos_sales.services.order_service import calculate_commission
def test_commission():
    o = Order(product="x", cost=10, price=20, channel="site")
    assert calculate_commission(o)==1.0
