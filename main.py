"""
Backward compatibility wrapper for development.
For production use, run: todo-rest
"""

from todo_rest.app import app, main

if __name__ == "__main__":
    main()
