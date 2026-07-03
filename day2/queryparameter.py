from fastapi import FastAPI

app = FastAPI()

@app.get("/user")

def home(user_id :int):
       a = ["apple", "banana", "kela"]
       return {"user id" : a[user_id]}



# optinal parameter & default value
@app.get("/username")
def home(username :str = "Name is not provided"):
       return {"user id" : username}



#multiple query parameter
@app.get("/About")

def about(name:str=None , age :int = None):
       return {
              "name":name ,
              "age" : age
       }
        
