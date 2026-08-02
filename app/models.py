from sqlalchemy import Column,Integer, String, DECIMAL
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products" # ye tablename ek dm match hona chiye us tablename se jo tumne postgresql mei sql use krke bnaya tha

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(DECIMAL(10,2),nullable = False)
    stock = Column(Integer,nullable=False)
