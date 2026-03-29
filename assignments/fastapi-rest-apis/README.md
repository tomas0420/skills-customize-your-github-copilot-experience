# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement a basic REST API using FastAPI, including endpoint creation, request validation, and structured JSON responses.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Build a FastAPI application with endpoints to manage a simple collection of books.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`
- Implement `GET /` that returns a welcome JSON message
- Implement `GET /books` that returns a list of books
- Implement `GET /books/{book_id}` that returns one book by ID
- Return a clear error response when a book is not found

### 🛠️ Add Create and Update Functionality

#### Description
Extend the API to support creating and updating books using validated request bodies.

#### Requirements
Completed program should:

- Define a Pydantic model for book data validation
- Implement `POST /books` to add a new book
- Implement `PUT /books/{book_id}` to update an existing book
- Return appropriate HTTP status codes for success and errors
- Include at least 3 example requests in comments or a short section at the bottom of the file
