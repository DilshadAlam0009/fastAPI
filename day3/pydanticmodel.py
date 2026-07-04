from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() 
# class User(BaseModel):
#     name:str
#     age:int

# @app.post("/create_user")
# def create_user(user:User):
#     return {
#         "Data" : user
#     }
        

#multiple model 

class Adress(BaseModel):
    city:str
    state:str
    pin:int


class User(BaseModel):
    name:str
    age:int
    address:Adress

@app.post("/create_user")
def create_user(user:User):
    return {
        "Data" : user
    }  


class Useremp(BaseModel):
    name:str
    age:int
    salaray:int
    address:Adress

@app.post("/create_emp")
def create_emp(user:Useremp):
    return {
        "Data": user
    }
     
