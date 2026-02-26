from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class Item(BaseModel):
    name: str
    quantity: int
    price: float

class Order(BaseModel):
    order_id: int
    customer_name: str
    items: list[Item]

@app.post("/orders/")
async def create_order(order: Order):
    total = sum(item.quantity * item.price for item in order.items)
    return {
        "message": f"Order {order.order_id} placed successfully!",
        "customer": order.customer_name,
        "total_amount": total
    }