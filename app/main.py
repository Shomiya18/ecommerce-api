from fastapi import FastAPI,Depends
from app.schemas import ProductCreate, ProductResponse
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models import Product


# Basemodel is the parent class for all the models in FastAPI. 
# It is used to define the structure of the data that will be sent and received by the API.

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to ECommerce API!"}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {
        "product_id": product_id,
        "name": "Sample Product",
        "price": 99
    }


@app.get("/search")
def search_products(category: str, brand_name: str):
    return {
        "category": category,
        "brand": brand_name
        }

@app.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate,db:Session = Depends(get_db)):
    new_product = Product(
        name = product.name,
        price= product.price,
        stock = product.stock
    )

    db.add(new_product)             #object ko Session mein add karta hai.
    db.commit()                     #data postgresql mei save krta h 
    db.refresh(new_product)         #database se updated values lata h
    return new_product