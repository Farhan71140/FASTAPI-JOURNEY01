from fastapi import FastAPI
app=FastAPI()
@app.get("/student/{id}")
def get_student(id:int):
    return{"student_id": id}


#Point 1 - from fastapi import FastAPI
#Bringing the FastAPI tool into our file so we can use it  

#Point 2 - app = FastAPI()
#Creating our FastAPI application and storing it in a variable called app

#Point 3 - @app.get("/students/{id}")
#Creating a GET endpoint with URL /students/{id} where id is a path parameter that changes dynamically

#Point 4 - def get_student(id: int):
#Defining a function that runs when the URL is visited, id must match {id} in the URL and it only accepts numbers

#Point 5 - return {"student_id": id}
#Sending back the response as JSON to the browser with the id that came in the URL#