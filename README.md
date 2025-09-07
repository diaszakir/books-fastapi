# Books REST API project (FastAPI)

First REST project created on Python using:

- FastAPI - backend
- Pydantic - data validation
- Starlette

---

## Methods:

- GET `/books` - Get all books
- GET `/books/{book_id}` - Get book by ID
- GET `/books/` - Get book by rating
- GET `/books/publish/` - By published date
- POST `/create_book` - Create new book
- PUT `/books/update_book` - Update book information
- DELETE `/books/{book_id}` - Delete book

--- 
## How to launch?

First, create your virtual environment

```
python -m venv .venv
```

Second, install FastAPI
```
pip install fastapi[standard] pydantic[standard]
```

Third, launch project using uvicorn
```
uvicorn app:app --reload
```

---
## Swagger-UI

You can see all endpoints and test API typing in browser:

```
http:127.0.0.1:8000/docs
```

---