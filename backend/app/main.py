from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, crud, database

# create DB tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Lab/Classroom Allocation API (local)")

# allow Vite dev server origin
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.get("/allocations/", response_model=List[schemas.Allocation])
def read_allocations(db: Session = Depends(get_db)):
    return crud.get_allocations(db)

@app.post("/allocations/", response_model=schemas.Allocation)
def create_allocation(allocation: schemas.AllocationCreate, db: Session = Depends(get_db)):
    return crud.create_allocation(db, allocation)
