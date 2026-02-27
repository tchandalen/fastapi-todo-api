from fastapi import FastAPI
from src.controllers.auth import auth_router
from src.controllers.todo import todo_router
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(
    title='Example ToDo API',
    version='1.0.0',
    description='Example create to do list API with authentication'
)
app.include_router(auth_router)
app.include_router(todo_router)