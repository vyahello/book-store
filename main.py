import databases
import sqlalchemy

from fastapi import FastAPI, Request
from decouple import config

import uvicorn

DATABASE_URL = (
    f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@"
    "localhost:5433/store"
)

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


books = sqlalchemy.Table(
    "books",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("author", sqlalchemy.String),
    sqlalchemy.Column("pages", sqlalchemy.Integer),
)
readers = sqlalchemy.Table(
    "readers",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
)

readers_books = sqlalchemy.Table(
    "readers_books",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "book_id", sqlalchemy.ForeignKey("books.id"), nullable=False
    ),
    sqlalchemy.Column(
        "reader_id", sqlalchemy.ForeignKey("readers.id"), nullable=False
    ),
)

app = FastAPI()


@app.on_event("startup")
async def startup() -> None:
    """Start the database."""
    await database.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    """Stop the database."""
    await database.disconnect()


@app.get("/books/")
async def get_all_books() -> list:
    """List all books."""
    query = books.select()
    return await database.fetch_all(query)


@app.post("/books/")
async def create_book(request: Request) -> dict:
    """Create single book."""
    data = await request.json()
    query = books.insert().values(**data)
    last_record_id = await database.execute(query)
    return {"id": last_record_id}


@app.post("/readers/")
async def create_reader(request: Request) -> dict:
    """Create single reader."""
    data = await request.json()
    query = readers.insert().values(**data)
    last_record_id = await database.execute(query)
    return {"id": last_record_id}


@app.post("/read/")
async def read_book(request: Request) -> dict:
    """Read single book."""
    data = await request.json()
    query = readers_books.insert().values(**data)
    last_record_id = await database.execute(query)
    return {"id": last_record_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
