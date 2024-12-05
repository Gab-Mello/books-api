# Book and Author Management API

## Overview
This project is a **RESTful API for managing books and authors**, developed to consolidate my studies in **Django** and **Django REST Framework (DRF)**. The API uses **Function-Based Views (FBVs)** to provide CRUD operations for books and authors.

---

## Features

### Books
- List all books.
- Create a new book.
- Retrieve a specific book by ID.
- Update book details (full or partial update).
- Delete a book.

### Authors
- List all authors.
- Create a new author.
- Retrieve a specific author by ID.
- Update author details (full or partial update).
- Delete an author.

---

## Technologies Used
- **Python**
- **Django**
- **Django REST Framework**

---

## Endpoints

### Books
- **GET /api/books/**: List all books.
- **POST /api/books/**: Create a new book.
- **GET /api/books/<id>/**: Retrieve a specific book.
- **PUT /api/books/<id>/**: Update a book completely.
- **PATCH /api/books/<id>/**: Update a book partially.
- **DELETE /api/books/<id>/**: Delete a book.

### Authors
- **GET /api/authors/**: List all authors.
- **POST /api/authors/**: Create a new author.
- **GET /api/authors/<id>/**: Retrieve a specific author.
- **PUT /api/authors/<id>/**: Update an author completely.
- **PATCH /api/authors/<id>/**: Update an author partially.
- **DELETE /api/authors/<id>/**: Delete an author.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
