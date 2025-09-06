from fastapi import FastAPI, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from starlette import status

# Creating app
app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    published_date: int
    description: str
    rating: int

    def __init__(self, id, title, author, published_date, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.published_date = published_date
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed", default=None) # we will use auto-increment
    title: str = Field(min_length=4)
    author: str = Field(min_length=4)
    published_date: int = Field(gt=1899, lt=2100)
    description: str = Field(max_length=100)
    rating: int = Field(gt=0, lt=6)

    model_config = {
        "json_scheme_extra": {
            "title": "Atomic Habits",
            "author": "James Clear",
            "published_date": 2018,
            "description": "A book about how to implement good habits",
            "rating": 5
        }
    }

# Test data
books = [
    Book(1, "Test", "Test", 2000, "Test", 5)
]

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return books


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book_by_id(book_id: int = Path(gt=0)): # if below 0, error 404
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(rating: int = Query(gt=0, lt=6)):
    return [book for book in books if book.rating == rating]


@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_book_by_publish_date(published_date: int = Query(gt=1899, lt=2100)):
    return [book for book in books if book.published_date == published_date]


@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    books.append(find_book_by_id(new_book))


def find_book_by_id(book: Book):
    book.id = 1 if len(books) == 0 else books[-1].id + 1
    return book