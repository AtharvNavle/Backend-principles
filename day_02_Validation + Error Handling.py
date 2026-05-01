from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

#storage of users
users_db = []

class Users(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=3, max_length=30)
    email: EmailStr
    age: int = Field(ge=18, le=100)

@app.get("/")
async def root():
    return {"message":"this is the root of the webpage"}

#creating user
@app.post("/users", status_code=201, response_model=Users)
async def validate_users(user: Users):
    existing_user = next((u for u in users_db if u["id"] == user.id), None)
    if existing_user is not None:
        raise HTTPException(status_code=400, detail="User with this id already exists")

    user_dict = user.model_dump()
    users_db.append(user_dict)
    return user

@app.get("/users/{user_id}", response_model=Users)
async def get_users(user_id: int):
    user = next((user for user in users_db if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users", response_model=list[Users])
async def get_all_users():
    return users_db



