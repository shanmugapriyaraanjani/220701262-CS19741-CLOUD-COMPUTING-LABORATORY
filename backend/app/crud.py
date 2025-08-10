from sqlalchemy.orm import Session
from . import models, schemas

def get_allocations(db: Session):
    return db.query(models.Allocation).all()

def create_allocation(db: Session, allocation: schemas.AllocationCreate):
    db_obj = models.Allocation(**allocation.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
