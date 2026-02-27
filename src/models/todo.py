from pydantic import BaseModel, Field

class CreateTodoRequest(BaseModel):
    title: str = Field(..., max_length=255)


class TodoResponse(BaseModel):
    id: str
    creator_id: str
    title: str
    is_completed: bool
    created_at: str
