from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

# Crear tablas automáticamente
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# conexión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET ALL
@app.get("/productos")
def read_productos(db: Session = Depends(get_db)):
    return crud.get_productos(db)

# GET BY ID
@app.get("/productos/{id}")
def read_producto(id: int, db: Session = Depends(get_db)):
    producto = crud.get_producto(db, id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

# CREATE
@app.post("/productos")
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.create_producto(db, producto)

# UPDATE
@app.put("/productos/{id}")
def update_producto(id: int, producto: schemas.ProductoUpdate, db: Session = Depends(get_db)):
    updated = crud.update_producto(db, id, producto)
    if not updated:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return updated

# DELETE
@app.delete("/productos/{id}")
def delete_producto(id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_producto(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Eliminado correctamente"}