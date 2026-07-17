from sqlalchemy.orm import Session
import models, schemas

def get_productos(db: Session):
    return db.query(models.Producto).all()

def get_producto(db: Session, producto_id: int):
    return db.query(models.Producto).filter(models.Producto.id == producto_id).first()

def create_producto(db: Session, producto: schemas.ProductoCreate):
    db_producto = models.Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def update_producto(db: Session, producto_id: int, producto: schemas.ProductoUpdate):
    db_producto = get_producto(db, producto_id)
    if db_producto:
        db_producto.nombre = producto.nombre
        db_producto.precio = producto.precio
        db_producto.cantidad = producto.cantidad
        db.commit()
        db.refresh(db_producto)
    return db_producto

def delete_producto(db: Session, producto_id: int):
    db_producto = get_producto(db, producto_id)
    if db_producto:
        db.delete(db_producto)
        db.commit()
    return db_producto