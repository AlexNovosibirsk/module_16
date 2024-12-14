# Задача "Модель пользователя":
from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    username: str = Field(..., min_length=5, max_length=25, description="Имя пользователя")
    age: int = Field(ge=18, le=100, description="Возраст пользователя")

class UserCreate(BaseModel):
    username: str = Field(..., min_length=5, max_length=25, description="Имя пользователя")
    age: int = Field(ge=18, le=100, description="Возраст пользователя")

users: List = [User(id=1, username="Ivan Co", age=22)]
# users: List = []


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/user")
async def create_user(user: UserCreate):
    new_id = max((user.id for user in users), default=0) + 1
    new_user = User(id=new_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    for user_obj in users:
        if user_obj.id == user_id:
            user_obj.username = user.username
            user_obj.age = user.age
            return user_obj
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int):
    for i, user_obj in enumerate(users):
        if user_obj.id == user_id:
            del users[i]
            return user_obj
    raise HTTPException(status_code=404, detail="User was not found")


# uvicorn module_16_4:app --reload

