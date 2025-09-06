from fastapi import FastAPI, Body, Query, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Book:
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
    rating: str = Field(gt=0, lt=6)

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
books = []