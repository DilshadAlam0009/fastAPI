from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{user_id}")
#{user_id}   this is known as path parameter 

def home(user_id :int):
       a = ["apple", "banana", "kela"]
       return {"user id" : a[user_id]}

# user_id :int := inout validation here