from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Product model
class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

# In-memory database
products_db: Dict[int, Product] = {}

# CREATE (POST)
@app.post("/products")
def create_product(product: Product):
    if product.id in products_db:
        raise HTTPException(status_code=400, detail="Product already exists")
    products_db[product.id] = product
    return {"message": "Product created successfully", "product": product}

# READ (GET by ID)
@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[product_id]

# READ ALL (GET all products)
@app.get("/products")
def get_all_products():
    return products_db

# UPDATE (PUT)
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    products_db[product_id] = product
    return {"message": "Product updated successfully", "product": product}

# DELETE
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    deleted_product = products_db.pop(product_id)
    return {"message": "Product deleted successfully", "product": deleted_product}