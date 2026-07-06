from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()
todos = []
def update(l):
    with open("database.json", 'w') as fs:
        json.dump(l,fs)


with open("database.json") as fs:
    todos = json.load(fs)




class Todo(BaseModel):
    id:int
    learn:str
    progress:str

@app.post("/todo")
def create_todo(todo:Todo):
    todos.append(todo.model_dump())
    update(todos)
    return {
        "messege" : "created sucessfully",
        "data" : todo
    }

@app.get("/todo")
def get_users():
    return todos

@app.get("/todo/{user_id}")
def get_user(user_id:int):
    for i in todos:
        if i["id"] == user_id:
            return {"data" : i}
    return {"eror" : "not found"}



@app.put("/todo/{user_id}")
def update_user(user_id:int, updated_data:Todo):
    for i , j in enumerate(todos):
        if j["id"] == user_id:
            todos[i] = updated_data.model_dump()
            update(todos)
            return {"messege" : "updated sucessfulyy",
                    "data" : updated_data
                    }
    return {"messege" : "id not found"}


@app.delete("/todo/{user_id}")
def delete_user(user_id:int):
    for i ,j in enumerate(todos):
        if j["id"] == user_id:
            todos.pop(i)
            update(todos)
            return {"messege" : "deleted Sucessfully"}
    return {"messege" : "todo not found"}




