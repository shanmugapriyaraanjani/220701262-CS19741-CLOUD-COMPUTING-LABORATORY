from sqlalchemy import Column, Integer, String
from .database import Base

class Allocation(Base):
    __tablename__ = "allocations"
    id = Column(Integer, primary_key=True, index=True)
    lab_or_classroom = Column(String, index=True)
    subject = Column(String)
    faculty = Column(String)
    time = Column(String)
