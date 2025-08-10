from pydantic import BaseModel

class AllocationBase(BaseModel):
    lab_or_classroom: str
    subject: str
    faculty: str
    time: str

class AllocationCreate(AllocationBase):
    pass

class Allocation(AllocationBase):
    id: int
    class Config:
        orm_mode = True
