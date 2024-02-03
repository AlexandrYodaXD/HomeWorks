from typing import List

from fastapi import FastAPI
from fastapi.responses import RedirectResponse, JSONResponse

from models.db_model import database, tasks
from models.pd_model import Task, TaskNew

app = FastAPI()


#  Подключение к базе данных
@app.on_event("startup")
async def startup():
    await database.connect()


#  Отключение от базы данных
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


#  Перенаправление на /tasks
@app.get("/")
async def root():
    return RedirectResponse("/tasks")


#  Получение списка задач
@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    query = tasks.select()
    return await database.fetch_all(query)


#  Получение задачи по id
@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    task = await database.fetch_one(query)
    if task:
        return await task
    return JSONResponse(status_code=404, content={"message": "Task not found"})


#  Создание новой задачи
@app.post("/tasks", response_model=Task)
async def create_task(task: TaskNew):
    query = tasks.insert().values(
        name=task.name,
        description=task.description,
        status_complete=task.status_complete,
    )
    last_record_id = await database.execute(query)

    return {"id": last_record_id, **task.dict()}


#  Обновление задачи по id
@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskNew):
    query = tasks.select().where(tasks.c.id == task_id)
    task_exists = await database.fetch_one(query)

    if task_exists:
        query = tasks.update().where(tasks.c.id == task_id).values(
            name=task.name,
            description=task.description,
            status_complete=task.status_complete,
        )
        await database.execute(query)
        return {"id": task_id, **task.dict()}

    return JSONResponse(status_code=404, content={"message": "Task not found"})


#  Удаление задачи по id
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    task_exists = await database.fetch_one(query)

    if task_exists:
        query = tasks.delete().where(tasks.c.id == task_id)
        await database.execute(query)
        return {"message": "Task deleted successfully"}

    return JSONResponse(status_code=404, content={"message": "Task not found"})


#  Заполнение базы данных фейковыми задачами
@app.get("/fill_fake_tasks/{count}")
async def fill_fake_tasks(count: int):
    for i in range(count):
        query = tasks.insert().values(
            name=f"Task {i + 1}",
            description=f"Description of task {i + 1}",
            status_complete=bool(i % 2),
        )
        await database.execute(query)
    return {"message": f"{count} fake tasks created"}
