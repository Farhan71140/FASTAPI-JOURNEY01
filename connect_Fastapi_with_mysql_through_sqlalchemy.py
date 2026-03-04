from fastapi import FastAPI, HTTPException, Depends  # 👈 add Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session  # 👈 add Session

app = FastAPI()

DATABASE_URL = "mysql+pymysql://root:91330@localhost:3306/student_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

class StudentDB(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    email = Column(String(100))

Base.metadata.create_all(bind=engine)

class Student(BaseModel):
    id: int
    name: str
    age: int
    email: str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@app.post("/students/")
def create_student(student: Student, db: Session = Depends(get_db)):  # 👈 Depends
    db_student = StudentDB(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"message": f"Student {student.name} created successfully!"}

# READ ALL
@app.get("/students/")
def get_students(db: Session = Depends(get_db)):  # 👈 Depends
    return db.query(StudentDB).all()

# READ ONE
@app.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):  # 👈 Depends
    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# UPDATE
@app.put("/students/{student_id}")
def update_student(student_id: int, updated: Student, db: Session = Depends(get_db)):  # 👈 Depends
    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    for key, value in updated.dict().items():
        setattr(student, key, value)
    db.commit()
    return {"message": f"Student {student_id} updated successfully!"}

# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):  # 👈 Depends
    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": f"Student {student_id} deleted successfully!"}