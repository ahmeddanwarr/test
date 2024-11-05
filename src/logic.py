from sqlalchemy.orm import Session
from src.model import Product
from uuid import UUID
from src.schemas import ProductCreate

def create_product(db: Session, product: ProductCreate):
    db_product = db.query(Product).filter(Product.guid == product.guid).first()
    
    if db_product:
        db_product.price = product.price
        db.commit()
        db.refresh(db_product)
    else:
        db_product = Product(guid=product.guid, price=product.price)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
    
    return db_product


def get_product(db: Session, guid: UUID):
    return db.query(Product).filter(Product.guid == guid).first()
