# Задача "Список пользователей в шаблоне":

from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from typing import Annotated, List
from starlette.templating import Jinja2Templates

# pip install Jinja2
# pip install aiofiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    username: str = Field(..., min_length=5, max_length=25, description="Имя пользователя")
    age: int = Field(ge=18, le=100, description="Возраст пользователя")


class UserCreate(BaseModel):
    username: str = Field(..., min_length=5, max_length=25, description="Имя пользователя")
    age: int = Field(ge=18, le=100, description="Возраст пользователя")


users: List = [
                User(id=1, username="Ivan Co", age=19),
                User(id=2, username="UrbanUser", age=24),
                User(id=3, username="UrbanTest", age=22),
                User(id=4, username="Capybara", age=60),
                User(id=17, username="SuperUSER", age=25),
                User(id=10, username="Alexander", age=35)
              ]


@app.get("/")
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}")
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        for user in users:
            if user.id == user_id:
                return templates.TemplateResponse("users.html", {"request": request, "user": user})
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


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

# uvicorn module_16_5:app --reload
