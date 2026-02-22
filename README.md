# Todo List REST API

A simple todo list application with REST endpoints and a web dashboard.

## Installation

```bash
pip install todo-rest```

## Running the App

After installation, you can run the app with the installed command:
```bash
todo-rest
```

Or using the development commands:
```bash
uv run python main.py
```

Or with uvicorn directly (with auto-reload for development):
```bash
uv run uvicorn todo_rest.app:app --reload
```

The API will be available at http://localhost:8000

## Dashboard

Open http://localhost:8000 in your browser to view the todo dashboard. The dashboard shows:
- Total tasks, completed, and pending counts
- All todos with their status
- Auto-refreshes every 5 seconds

## API Endpoints

### Get all todos
```
GET /todos
```

### Get a specific todo
```
GET /todos/{id}
```

### Create a new todo
```
POST /todos
Content-Type: application/json

{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false
}
```

### Update a todo
```
PUT /todos/{id}
Content-Type: application/json

{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread, cheese",
  "completed": true
}
```

### Delete a todo
```
DELETE /todos/{id}
```

## Interactive API Documentation

FastAPI provides automatic interactive documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
