from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class Address(BaseModel):
    street: str
    city: str
    zipcode: str

class Student(BaseModel):
    id: int
    name: str
    age: int
    email: Optional[str] = None
    address: Optional[Address] = None

@app.post("/students/")
async def register_student(student: Student):
    return {
        "message": f"Student {student.name} registered successfully!",
        "details": student
    }