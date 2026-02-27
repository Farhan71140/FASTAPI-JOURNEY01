from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    role: str

# Fake in-memory database
users_db: Dict[int, User] = {
    1: User(id=1, name="Alice", role="Admin"),
    2: User(id=2, name="Bob", role="Intern")
}

# DELETE method: Remove a user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id in users_db:
        deleted_user = users_db.pop(user_id)  # remove from dictionary
        return {"message": "User deleted successfully", "user": deleted_user}
    else:
        raise HTTPException(status_code=404, detail="User not found")