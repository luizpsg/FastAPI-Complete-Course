from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    def __init__(self, id: int, title: str, author: str, description: str, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = (
        Field(
            title="The ID of the book", description="This is an auto-generated field"
        ),
        None,
    )
    title: str = Field(min_length=3, max_length=50)
    author: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=5, max_length=100)
    rating: int = Field(ge=1, le=5)


BOOKS = [
    Book(1, "War and Peace", "Leo Tolstoy", "Epic novel about Russian society", 5),
    Book(2, "Pride and Prejudice", "Jane Austen", "British novel about love", 5),
    Book(3, "Crime and Punishment", "Fyodor Dostoevsky", "Psychological novel", 4),
    Book(4, "Wuthering Heights", "Emily Bronte", "Gothic novel", 2),
    Book(5, "Anna Karenina", "Leo Tolstoy", "Russian novel about love and society", 5),
    Book(6, "To Kill a Mockingbird", "Harper Lee", "American novel", 4),
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create_book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    return new_book


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
