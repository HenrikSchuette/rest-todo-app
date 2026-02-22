from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
from pathlib import Path

app = FastAPI(title="Todo List API")

# Mount static files
static_dir = Path(__file__).parent / "static"
static_dir.mkdir(exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# In-memory storage
todos = {}
next_id = 1


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False


@app.get("/")
def root():
    """Serve the dashboard"""
    return FileResponse(static_dir / "index.html")


@app.get("/todos", response_model=list[Todo])
def get_todos():
    """Get all todos"""
    return list(todos.values())


@app.get("/todo/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    """Get a specific todo by ID"""
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]


@app.post("/todo", response_model=Todo, status_code=201)
def create_todo(todo: TodoCreate):
    """Create a new todo"""
    global next_id
    new_todo = Todo(
        id=next_id,
        title=todo.title,
        description=todo.description,
        completed=todo.completed
    )
    todos[next_id] = new_todo
    next_id += 1
    return new_todo


@app.put("/todo/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: TodoCreate):
    """Update an existing todo"""
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    updated_todo = Todo(
        id=todo_id,
        title=todo.title,
        description=todo.description,
        completed=todo.completed
    )
    todos[todo_id] = updated_todo
    return updated_todo


@app.delete("/todo/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    """Delete a todo"""
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
    return None


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
