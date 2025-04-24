
from fastapi import APIRouter, HTTPException
from agentos_sales.models.order_model import Order
from agentos_sales.services.order_service import create_order, list_orders, calculate_commission

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/")
def create(o: Order):
    order = create_order(o)
    return order

@router.get("/")
def all_orders():
    return list_orders()

@router.get("/{order_id}/commission")
def commission(order_id: str):
    orders = {o.id:o for o in list_orders()}
    if order_id not in orders:
        raise HTTPException(status_code=404, detail="not found")
    return {"commission": calculate_commission(orders[order_id])}
