from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Student model
class Student(BaseModel):
    id: int
    name: str
    age: int
    email: Optional[str] = None

# Example "database"
students_db = {
    1: Student(id=1, name="Farhan", age=22, email="farhan@example.com"),
    2: Student(id=2, name="Ayesha", age=20, email="ayesha@example.com"),
    3: Student(id=3, name="Rahul", age=23, email="rahul@example.com"),
    4: Student(id=4, name="Sneha", age=21, email="sneha@example.com")
}

# CREATE (POST)
@app.post("/students/")
async def create_student(student: Student):
    if student.id in students_db:
        raise HTTPException(status_code=400, detail="Student with this ID already exists")
    students_db[student.id] = student
    return {"message": f"Student {student.name} created successfully!"}

# READ ALL (GET)
@app.get("/students/")
async def get_students():
    return students_db

# READ ONE (GET by ID)
@app.get("/students/{student_id}")
async def get_student(student_id: int):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# UPDATE (PUT)
@app.put("/students/{student_id}")
async def update_student(student_id: int, updated_student: Student):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    students_db[student_id] = updated_student
    return {"message": f"Student {student_id} updated successfully!"}

# DELETE (DELETE)
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    del students_db[student_id]
    return {"message": f"Student {student_id} deleted successfully!"}