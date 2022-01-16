import pytest
from fastapi.testclient import TestClient

from main import app

URL = 'http://0.0.0.0:8000'


@pytest.fixture
def client() -> TestClient:
    with TestClient(app) as cl:
        yield cl


def test_all_books(client: TestClient) -> None:
    books = client.get(f"{URL}/books").json()
    assert isinstance(books, list)
    assert books


def test_create_book(client: TestClient) -> None:
    res = client.post(
        f'{URL}/books', json={'title': 'Title', 'author': 'Tuthor', 'pages': 10}
    )
    assert res.status_code == 307


def test_create_reader(client: TestClient) -> None:
    res = client.post(
        f'{URL}/readers', json={'first_name': 'John', 'last_name': 'Om'}
    )
    assert res.status_code == 307


def test_read_book(client: TestClient) -> None:
    res = client.post(f'{URL}/readers', json={'book_id': 1, 'reader_id': 1})
    assert res.status_code == 307
