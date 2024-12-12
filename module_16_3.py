# Задача "Имитация работы с БД"

from fastapi import FastAPI
from typing import Annotated
from fastapi import Path
from fastapi import HTTPException

app = FastAPI()
users = {'1': 'Имя: Дима, возраст: 18',
         '2': 'Имя: Пётр, возраст: 19',
         '3': 'Имя: Вася, возраст: 20'}
# 1. Read (GET):
@app.get("/")  # http:/127.0.0.1:8000/
async def get_main_page() -> dict:
    return users


# 2. Create (POST):
@app.post("/users/{username}/{age}")
async def post_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=34)]):

    new_index = str(len(users) + 1)
    users.update({new_index: f"Имя: {username}, возраст: {age}"})
    return users


# 3. Update (PUT):
@app.put("/users/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    for key, _ in users.items():
        if key == user_id:
            users.update({user_id: f"Имя: {username}, возраст: {age}"})
            break
        else:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
    return users


# 4. Delete (DELETE):
@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    for key, _ in users.items():
        if key == user_id:
            users.pop(user_id)
            break
        else:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
    return users

# uvicorn module_16_3:app --reload
