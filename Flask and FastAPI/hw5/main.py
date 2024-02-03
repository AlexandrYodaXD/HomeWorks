from typing import List

from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse

from models import Task

app = FastAPI()

tasks = [
    Task(id=1, name="Task 1", description="Description 1", status_complete=False),
    Task(id=2, name="Task 2", description="Description 2", status_complete=True),
]


#  Перенаправление на /tasks
@app.get("/")
async def root():
    return RedirectResponse("/tasks")


#  Получение списка задач
@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks


#  Получение задачи по id
@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    # Поиск задачи по указанному id
    for task in tasks:
        if task.id == task_id:
            return task
    # Если задача с указанным id не найдена, возвращаем ошибку 404
    return JSONResponse(status_code=404, content={"message": "Task not found"})


#  Создание новой задачи
@app.post("/tasks")
async def create_task(task: Task):
    # Проверка на уникальность id
    if task.id is not None and any(existing_task.id == task.id for existing_task in tasks):
        return JSONResponse(status_code=400, content={"message": "Task with this id already exists"})

    # Если id не передан, то генерируем его
    if not task.id:
        task.id = max(task.id for task in tasks) + 1 if tasks else 1

    new_task = Task(id=task.id, name=task.name, description=task.description, status_complete=task.status_complete)
    tasks.append(new_task)

    return new_task


#  Обновление задачи по id
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    # Поиск задачи по указанному id
    for task in tasks:
        if task.id == task_id:
            task.name = task.name
            task.description = task.description
            task.status_complete = task.status_complete
            return task
    # Если задача с указанным id не найдена, возвращаем ошибку 404
    return JSONResponse(status_code=404, content={"message": "Task not found"})


#  Удаление задачи по id
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    # Поиск задачи по указанному id
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            return {"message": "Task deleted successfully"}
    # Если задача с указанным id не найдена, возвращаем ошибку 404
    return JSONResponse(status_code=404, content={"message": "Task not found"})
