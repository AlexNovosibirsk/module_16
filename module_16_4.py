# Задача "Модель пользователя":

from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


users: List = [User(id=1, username="ASD", age=22)]


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username, age):
    new_id = max((user.id for user in users), default=0) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_task(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_model=User)
async def delete_task(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# uvicorn module_16_4:app --reload
