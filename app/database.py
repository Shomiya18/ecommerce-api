from sqlalchemy import create_engine #this is used to create the connection between python and postgresql
from sqlalchemy.orm import sessionmaker #this creates session mtlb the actually communication
from app.models import Base

DATABASE_URL = "postgresql://shomiyachaturvedi@localhost/ecommerce_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind = engine)

Base.metadata.create_all(bind = engine)  ## it creates all the table which are not created but have used the base to create their models