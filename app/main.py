from fastapi import FastAPI

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
def search_products(category: str):
    return {"category": category}