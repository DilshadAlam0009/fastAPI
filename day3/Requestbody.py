from fastapi import FastAPI

app = FastAPI()
@app.post("/create_user")

def create_user(user:dict):
    return {
        "messege" : "successfully created",
        "Data" : user
        }