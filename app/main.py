from fastapi import FastAPI,Depends , HTTPException  #depends help krta h baar baar session create krne ka code nhi likhna pdta 
from app.schemas import ProductCreate, ProductResponse, UserCreate, UserResponse, LoginRequest
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models import Product,User 
from app.auth import hash_password, verify_password


# Basemodel is the parent class for all the models in FastAPI. 
# It is used to define the structure of the data that will be sent and received by the API.

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to ECommerce API!"}

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

@app.get("/products",response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

@app.get("/products/{product_id}", response_model= ProductResponse)
def get_product(product_id: int,db: Session = Depends(get_db)):

    product = db.query(Product).filter(Product.id == product_id).first()

    if(product == None):
        raise HTTPException(
            status_code = 404,
            detail = "Product not found"
        )
    return product

@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, Updatedproduct: ProductCreate, db:Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()

    if product == None:
        raise HTTPException(
            status_code= 404,
            detail= " Product not found"
        )

    product.name = Updatedproduct.name
    product.price = Updatedproduct.price
    product.stock = Updatedproduct.stock

    db.commit()
    db.refresh(product)

    return product


@app.delete("/products/{product_id}", response_model= ProductResponse)
def product_delete(product_id = int, db :Session = Depends(get_db)):

    product = db.query(Product).filter(Product.id == product_id).first()

    if product == None:
        raise HTTPException(
            status_code= 404,
            detail= "Product not found"
        )
    
    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}

@app.get("/products/filter", response_model= list[ProductResponse])
def filter_product(min_price :float, db: Session= Depends(get_db)):
    products = db.query(Product).filter(Product.price>min_price).all()
    return products

@app.post("/register", response_model= UserResponse)
def register(user: UserCreate,db: Session = Depends(get_db)):
    
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
            raise HTTPException(
                status_code= 400,
                detail= "Email already registered"
            )
    
    new_user = User(
            user_name = user.user_name,
            email = user.email,
            password = hash_password(user.password)
        )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.post("/login")
def login(user: LoginRequest, db : Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if db_user is None:
        raise HTTPException(
            status_code= 401,
            detail= "Invalid Credentials"
        )

    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code = 401
            detail = "Invalid Credentials"
        )

    

