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
async def get_users() -> dict:
    return users


# 2. Create (POST):
@app.post("/users/{username}/{age}")
async def post_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=100, description="Enter age", example=34)]) -> str:

    if users:
        keys_digit = [int(key_char) for key_char, _ in users.items()]
        user_id = str(max(keys_digit) + 1)
    else:
        user_id = '1'

    users.update({user_id: f"Имя: {username}, возраст: {age}"})
    return f"User {user_id} is registered"


# 3. Update (PUT):
@app.put("/users/{user_id}/{username}/{age}")
async def update_user(user_id: str,
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=100, description="Enter age", example=34)]) -> str:
    for key, _ in users.items():
        if key == user_id:
            users.update({user_id: f"Имя: {username}, возраст: {age}"})
            return f"User {user_id} has been updated"
    raise HTTPException(status_code=404, detail="user not found")


# 4. Delete (DELETE):
@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    try:
        users.pop(user_id)
    except KeyError as err:
        raise HTTPException(status_code=404, detail=f"user not found, KeyError {err}")
    return f"User {user_id} has been deleted"


# uvicorn module_16_3:app --reload
