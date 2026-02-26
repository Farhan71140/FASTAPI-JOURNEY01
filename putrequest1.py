from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI()

# Define a User model
class User(BaseModel):
    id: int
    name: str
    role: Optional[str] = None   # role can be optional

# In-memory database
users_db: Dict[int, User] = {                         #- This is a type hint from Python’s typing module The keys of the dictionary are integers (int)  The values are User objects (instances of the Pydantic model User).
    1: User(id=1, name="Alice", role="Admin"),        # So users_db is a dictionary mapping user IDs (like 1, 2) to user data.
    2: User(id=2, name="Bob", role="Intern")          #- A type hint in Python is a way to tell the interpreter (and other developers) what type of data a variable, function parameter, or return value is expected to be.

}

# PUT method: Update or create user
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id in users_db:
        users_db[user_id] = user
        return {"message": "User updated successfully", "user": users_db[user_id]}
    else:
        users_db[user_id] = user
        return {"message": "User created successfully", "user": users_db[user_id]}