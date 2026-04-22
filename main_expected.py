from fastapi import FastAPI
from pydantic import BaseModel, EmailStr 

app = FastAPI()

#storage of users
users_db = []

class Users(BaseModel):
    id:int
    name:str
    email:EmailStr

@app.get("/")
async def root():
    return {"message":"this is the root of the webpage"}

#creating user
@app.post("/users")
async def create_users(user:User):
    user_dict = user.model_dump()
    users_db.append(user_dict)
    return user

@app.get("/users")
async def get_users():
    return users_db
