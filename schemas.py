from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    precio: int
    cantidad: int

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int

    class Config:
        orm_mode = True