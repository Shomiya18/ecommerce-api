from pydantic import BaseModel
# Basemodel is the parent class for all the models in FastAPI. 
# It is used to define the structure of the data that will be sent and received by the API.


class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int

class ProductResponse(BaseModel):
    name: str
    price: float