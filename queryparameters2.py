from fastapi import FastAPI
app=FastAPI()
@app.get("/students")
def get_students(city: str = "Hyderabad"):
    return {"city": city}