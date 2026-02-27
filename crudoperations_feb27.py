from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Pydantic model for user
class User(BaseModel):
    id: int
    name: str
    role: str

# In-memory database
users_db: Dict[int, User] = {}     #- users_db → This is the variable name for your in‑memory “database.” It’s just a Python dictionary.
                                  #  Dict[int, User] → This is a type hint from Python’s typing module.
                                     # It tells FastAPI (and other developers) what kind of data the dictionary will hold:
                                      # Keys are of type int (like 1, 2, 3 → user IDs).
                                    #Values are of type User (your Pydantic model with fields like id, name, role).
                                    #= {} → This initializes the dictionary as empty at the start. No users are stored until you add them with POST.
# CREATE (POST)
@app.post("/users")
def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.id] = user             #-  save the user in users_db.
    return {"message": "User created successfully", "user": user}

# READ (GET)
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

# UPDATE (PUT)
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = user
    return {"message": "User updated successfully", "user": user}

# DELETE
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = users_db.pop(user_id)
    return {"message": "User deleted successfully", "user": deleted_user}

