from fastapi import FastAPI
from pydantic import BaseModel 
from pydantic import EmailStr, Field

app = FastAPI()


#defining da model firstly
class User(BaseModel):
    id : int
    name : str
    email : EmailStr | None = Field(default = None)

users_db = []

@app.get("/")
async def root():
    return {"message":"woosah"}

@app.post("/users")
async def create_user(user: User):
    users_db.append(user)
    return {
        "id":user.id,
        "name":user.name,
        "email":user.email
    }

@app.get("/users")
async def get_user():
    return users_db