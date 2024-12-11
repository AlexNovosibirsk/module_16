
# Задача "Аннотация и валидация"

from fastapi import FastAPI
from typing import Annotated
from fastapi import Path

app = FastAPI()


@app.get("/")  # http:/127.0.0.1:8000/
async def get_main_page() -> str:
    return "Главная страница"


@app.get("/user/admin")  # http://127.0.0.1:8000/user/admin
async def get_admin_page() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")  # http://127.0.0.1:8000/user/123
async def get_user_number(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='7')]) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")  # http://127.0.0.1:8000/user?
async def get_user_info(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
                             age: Annotated[int, Path(ge=18, le=120,               description="Enter age",      example=34)]) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


# Операторы равенства:
# eq: проверяет, является ли поле равным постоянному значению.
# ne: проверяет, является ли поле не равным постоянному значению.
# Операторы диапазона:
# gt: проверяет, больше ли поле постоянного значения.
# lt: проверяет, меньше ли поле постоянного значения.
# ge: проверяет, больше или равно поле постоянному значению.
# le: проверяет, меньше или равно поле постоянному значению.


# uvicorn module_16_2:app --reload

