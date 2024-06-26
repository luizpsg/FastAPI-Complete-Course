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
    id: int
    title: str
    author: str
    description: str
    rating: int


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
    BOOKS.append(new_book)
    return new_book
