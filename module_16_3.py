# Задача "Имитация работы с БД"

from fastapi import FastAPI
from typing import Annotated
from fastapi import Path
from fastapi import HTTPException

app = FastAPI()
users = {'1': 'Имя: Дима, возраст: 18'}
# users = {'1': 'Имя: Дима, возраст: 18',
#          '2': 'Имя: Пётр, возраст: 19',
#          '3': 'Имя: Вася, возраст: 20'}

keys = [int(key) for key in users.keys()]
if keys:
    new_key = str(max(keys) + 1)
else:
    new_key = "1"
print(new_key)

# 1. Read (GET):
@app.get("/users")
async def get_users():
    return users


# 2. Create (POST):
@app.post("/users/{username}/{age}")
async def post_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=34)]):



    # new_id = max( int(user for user in users.get()))

    pass

    # new_id = max(task["id"] for task in tasks) + 1 if tasks else 1
    # new_task = {"id": new_id, "description": description}
    # tasks.append(new_task)
    # return new_task


# 3. Update (PUT):
@app.put("/users/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):
    pass
    # for task in tasks:
    #     if task["id"] == task_id:
    #         task["description"] = description
    #         return task
    # raise HTTPException(status_code=404, detail="Задача не найдена")


# 4. Delete (DELETE):
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    pass
    # for i, task in enumerate(tasks):
    #     if task["id"] == task_id:
    #         del tasks[i]
    #         return {"detail": "Задача удалена"}
    # raise HTTPException(status_code=404, detail="Задача не найдена")

# @app.get("/tasks/{task_id}")
# async def get_task(task_id: int):
#     pass
# for task in tasks:
#     if task["id"] == task_id:
#         return task
# raise HTTPException(status_code=404, detail="Задача не найдена")


# uvicorn module_16_3:app --reload
