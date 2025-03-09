from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, ConfigDict

router = APIRouter()

books = [
    {
        "id": 1,
        "title": "Асинхронность в Python",
        "author": "Мэттью",
    },
    {
        "id": 2,
        "title": "Backend разработка в Python",
        "author": "Артём",
    },
]

@router.get("/books", tags=["backend"])
async def get_books():
    return books

@router.delete("/books", tags=["backend"])
async def get_books():
    books.clear()
    return {"message": "Books deleted"}

@router.get("/books/{book_id}", tags=["backend"])
async def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found")

class Book(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)

    model_config = ConfigDict(extra="forbid")

@router.post("/books", tags=["backend"])
async def add_book(book: Book):
    books.append({
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author,
    })
    raise HTTPException(status_code=201, detail="Book added")
