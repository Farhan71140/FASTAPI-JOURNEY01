from fastapi import FastAPI
from pydantic import Basemodel
app=FastAPI()
class user(Basemodel):
    name:str
    age:int

@app.post("/users")
async def create_user(user: User):  #- defines an asynchronous function.
    # FastAPI uses async so it can handle many requests at the same time efficiently.
#create_user → the name of the function (you can choose any name).

 #- user → this is the parameter (the variable name) that will hold the data coming from the request bodyits the first user left side one 
  #the right side of the User is a pydantic model the first U is in capital letter 
  #- It means FastAPI expects the request body to match the User Pydantic model.
 # When JSON comes in, FastAPI + Pydantic will validate it and then give you a Python object called user.

 return{"message":f" my name is {user.name}, and age is {user.age}"}
           




       