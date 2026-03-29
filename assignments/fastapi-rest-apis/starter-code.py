# Starter Code for Building REST APIs with FastAPI

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Task 1: Create Core API Endpoints
# Use this in-memory list as your temporary data store.
books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 2, "title": "Automate the Boring Stuff", "author": "Al Sweigart"},
]


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Books API"}


@app.get("/books")
def get_books():
    # TODO: Return the full books list
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find and return one book by id
    # If not found, raise HTTPException(status_code=404, detail="Book not found")
    pass


# Task 2: Add Create and Update Functionality
class BookInput(BaseModel):
    title: str
    author: str


@app.post("/books")
def create_book(book: BookInput):
    # TODO: Create and append a new book with an auto-incremented id
    # Return the newly created book
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    # TODO: Update an existing book by id
    # If not found, raise HTTPException(status_code=404, detail="Book not found")
    pass


# Example test commands (after running: uvicorn starter-code:app --reload)
# curl http://127.0.0.1:8000/
# curl http://127.0.0.1:8000/books
# curl -X POST http://127.0.0.1:8000/books -H "Content-Type: application/json" -d '{"title":"Fluent Python","author":"Luciano Ramalho"}'
