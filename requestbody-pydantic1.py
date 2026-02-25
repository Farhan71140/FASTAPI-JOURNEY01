from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Step 1: Define a Pydantic model
class Student(BaseModel):
    id: int
    name: str
    age: int
    email: Optional[str] = None   # optional field
    is_active: bool = True        # default value

# Step 2: Use it in a POST endpoint
@app.post("/students/")
async def register_student(student: Student):
    return {
        "message": f"Student {student.name} registered successfully!",
        "details": {
            "id": student.id,
            "age": student.age,
            "email": student.email,
            "active": student.is_active
        }
    }