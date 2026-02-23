from fastapi import FastAPI
app=FastAPI()

@app.get("/students")
def get_students(city: str, age: int):
    return {"city": city, "age": age}
