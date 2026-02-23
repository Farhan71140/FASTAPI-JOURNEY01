from fastapi import FastAPI
app=FastAPI()
@app.get("/student/{name}")
def get_student(name:str):
    return{"student_name":name}      #The student_name in return is just a KEY name — you can name it anything you want!





