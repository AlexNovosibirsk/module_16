# Задача "Начало пути":

from fastapi import FastAPI

app = FastAPI()


# 2.Создайте маршрут к главной странице - "/".
# По нему должно выводиться сообщение "Главная страница".
@app.get("/")  # http:/127.0.0.1:8000/
async def get_main_page() -> str:
    return "Главная страница"


# 3.Создайте маршрут к странице администратора - "/user/admin".
# По нему должно выводиться сообщение "Вы вошли как администратор".
@app.get("/user/admin")  # http://127.0.0.1:8000/user/admin
async def get_admin_page() -> str:
    return "Вы вошли как администратор"


# 4.Создайте маршрут к страницам пользователей используя параметр в пути - "/user/{user_id}".
# По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>".
@app.get("/user/{user_id}")  # http://127.0.0.1:8000/user/123
async def get_user_number(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"


# 5.Создайте маршрут к страницам пользователей передавая данные в адресной строке - "/user".
# По нему должно выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".
@app.get("/user")  # http://127.0.0.1:8000/user?
async def get_user_info(username: str = "Alex", age: int = 12) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


# uvicorn module_16_1:app --reload
