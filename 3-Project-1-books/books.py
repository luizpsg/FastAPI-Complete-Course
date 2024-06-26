from fastapi import Body, FastAPI

app = FastAPI()


BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        title = book.get("title")
        if title and title.casefold() == book_title.casefold():
            return book
    return {"error": "Book not found"}, 404


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        cat = book.get("category")
        if cat and cat.casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/by-author/{author}")
async def read_author(author: str):
    books_to_return = []
    for book in BOOKS:
        auth = book.get("author")
        if auth and auth.casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/by-author/")
async def read_author(author: str):
    books_to_return = []
    for book in BOOKS:
        auth = book.get("author")
        if auth and auth.casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{author}/")
async def read_author_by_query(author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        auth = book.get("author")
        cat = book.get("category")
        if (
            auth
            and auth.casefold() == author.casefold()
            and cat
            and cat.casefold() == category.casefold()
        ):
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return new_book


@app.put("/books/update_book")
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == update_book.get("title").casefold():
            BOOKS[i] = update_book
            return update_book
    return {"error": "Book not found"}, 404


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            deleted_book = BOOKS.pop(i)
            return deleted_book
    return {"error": "Book not found"}, 404
