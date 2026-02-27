from fastapi import APIRouter, Depends, Body
from bson import ObjectId

from src.depends.security import is_valid_token
from src.services.todo import insert_todo, find_by_id, find_all
from src.models.todo import CreateTodoRequest, TodoResponse


todo_router = APIRouter(tags=['Todo'])


@todo_router.post(
    '/api/todo',
    summary='to create new todo'
)
async def store(
    data: dict = Depends(is_valid_token),
    body: CreateTodoRequest = Body()
) -> TodoResponse:
    oid = insert_todo(body.title, ObjectId(data['id']))
    todo = find_by_id(oid)
    return TodoResponse(
        id=str(todo['_id']),
        creator_id=str(todo['creator_id']),
        title=todo['title'],
        is_completed=todo['is_completed'],
        created_at=str(todo['created_at'])
    )


@todo_router.get(
    '/api/todo',
    summary='to get all todo',
)
async def get_all(
    data = Depends(is_valid_token)
):
    todos = find_all(ObjectId(data['id']))
    res_todos = []
    for todo in todos:
        temp = TodoResponse(
            id=str(todo['_id']),
            creator_id=str(todo['creator_id']),
            title=todo['title'],
            is_completed=todo['is_completed'],
            created_at=str(todo['created_at'])
        )
        res_todos.append(temp)

    return res_todos


@todo_router.put(
    '/api/todo/{id}',
    summary='to update todo list',
    dependencies=[Depends(is_valid_token)]
)
async def update():
    return 'Update todo'



@todo_router.delete(
    '/api/todo/{id}',
    summary='to delete todo',
    dependencies=[Depends(is_valid_token)]
)
async def destroy():
    return 'Delete todo'