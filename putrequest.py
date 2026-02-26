from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    role: str   # all fields required

users_db = {}   # no Dict type hint       

@app.put("/users/{user_id}")    #- This defines a PUT endpoint at the URL /users/{user_id}.
                                 # {user_id} is a path parameter — when you call /users/2, FastAPI passes user_id = 2 into the function.

def update_user(user_id: int, user: User):    #- This is the function that runs when someone calls the endpoint.
    if user_id in users_db:       #- users_db is our fake database (a dictionary).
                                    # This line checks if the given user_id already exists in the dictionary.

        users_db[user_id] = user
        return {"message": "User updated successfully", "user": users_db[user_id]}
    else:
        users_db[user_id] = user
        return {"message": "User created successfully", "user": users_db[user_id]}