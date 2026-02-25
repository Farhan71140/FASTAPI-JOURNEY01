from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None

@app.post("/products/")
async def create_product(product: Product):
    return {
        "message": f"Product {product.name} created successfully!",
        "details": product
    }