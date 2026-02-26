from fastapi import FastAPI
from pydantic import Field
from typing import optional
from pydantic import BaseModel
app=FastAPI()

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    age: int = Field(..., ge=18, le=60)
    email: Optional[str] = None

@app.post("/users/")
async def create_user(user: User):
    return {"message": f"User {user.username} created successfully!"}