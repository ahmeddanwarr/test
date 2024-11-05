
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.logic import create_product, get_product
from src.model import SessionLocal
from src.schemas import ProductCreate, ProductResponse
from uuid import UUID

# Dependency for the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/products/", response_model=ProductResponse)
def create_product_endpoint(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)

@app.get("/products/{guid}", response_model=ProductResponse)
def read_product(guid: UUID, db: Session = Depends(get_db)):
    db_product = get_product(db=db, guid=guid)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

