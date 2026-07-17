from sqlalchemy import Column, Integer, String
from database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    precio = Column(Integer)
    cantidad = Column(Integer)