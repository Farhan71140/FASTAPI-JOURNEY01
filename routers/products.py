from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Product(BaseModel):
    id: int
    name: str
    price: float

products_db = {}

@router.post("/products")
def create_product(product: Product):
    if product.id in products_db:
        raise HTTPException(status_code=400, detail="Product already exists")
    products_db[product.id] = product
    return {"message": "Product created", "product": product}

@router.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[product_id]