from typing import Optional
from fastapi import Body, FastAPI, Path
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    def __init__(
        self,
        id: int,
        title: str,
        author: str,
        description: str,
        rating: int,
        published_date: int,
    ):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(None, title="Id is not needed")
    title: str = Field(min_length=3, max_length=50)
    author: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=5, max_length=100)
    rating: int = Field(ge=1, le=5)
    published_date: int = Field(ge=1000, le=2024)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "A new book",
                "author": "Luiz Paulo Saud",
                "description": "A description of the book",
                "rating": 5,
                "published_date": 2021,
            }
        }


BOOKS = [
    Book(
        1, "War and Peace", "Leo Tolstoy", "Epic novel about Russian society", 5, 1869
    ),
    Book(2, "Pride and Prejudice", "Jane Austen", "British novel about love", 5, 1813),
    Book(
        3, "Crime and Punishment", "Fyodor Dostoevsky", "Psychological novel", 4, 1869
    ),
    Book(4, "Wuthering Heights", "Emily Bronte", "Gothic novel", 2, 1847),
    Book(
        5,
        "Anna Karenina",
        "Leo Tolstoy",
        "Russian novel about love and society",
        5,
        1877,
    ),
    Book(6, "To Kill a Mockingbird", "Harper Lee", "American novel", 4, 1960),
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/id/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    return {"error": "Book not found"}


@app.get("/books/")
async def read_book_by_rating(book_rating: int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.get("/books/published-date/{published_date}")
async def read_book_by_published_date(published_date: int):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return


@app.post("/create_book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    return new_book


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            return book
    return {"error": "Book not found"}


@app.delete("/books/delete/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            return {"message": "Book deleted"}
    return {"error": "Book not found"}
