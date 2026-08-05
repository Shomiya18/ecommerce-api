from sqlalchemy import Column,Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import DeclarativeBase,relationship



class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable = False)
    email = Column(String)
    products = relationship("Product", back_populates="owner")

class Product(Base):
    __tablename__ = "products" # SQLAlchemy will create a table in PostgreSQL with this name.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(DECIMAL(10,2),nullable = False)
    stock = Column(Integer,nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="products")
