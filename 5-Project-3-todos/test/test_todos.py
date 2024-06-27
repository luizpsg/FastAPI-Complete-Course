from routers.todos import get_db, get_current_user
from fastapi import status
from models import Todos
from utils import *

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_read_all_authenticated(test_todo):
    response = client.get("/todos/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "id": 1,
            "title": "Test Todo",
            "description": "Test Description",
            "priority": 1,
            "completed": False,
            "owner_id": 1,
        }
    ]


def test_read_one_authenticated(test_todo):
    response = client.get("/todos/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": 1,
        "title": "Test Todo",
        "description": "Test Description",
        "priority": 1,
        "completed": False,
        "owner_id": 1,
    }


def test_read_one_authenticated_not_found(test_todo):
    response = client.get("/todos/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}


def test_create_todo(test_todo):
    request_data = {
        "title": "New Todo",
        "description": "New Description",
        "priority": 2,
        "completed": False,
    }

    response = client.post("/todos/", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        "id": 2,
        "title": "New Todo",
        "description": "New Description",
        "priority": 2,
        "completed": False,
        "owner_id": 1,
    }


def test_update_todo(test_todo):
    request_data = {
        "title": "Updated Todo",
        "description": "Updated Description",
        "priority": 3,
        "completed": True,
    }

    response = client.put("/todos/1", json=request_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": 1,
        "title": "Updated Todo",
        "description": "Updated Description",
        "priority": 3,
        "completed": True,
        "owner_id": 1,
    }


def test_delete_todo(test_todo):
    response = client.delete("/todos/1")
    assert response.status_code == status.HTTP_200_OK
    db = TestingSessionLocal()
    todo = db.query(Todos).filter(Todos.id == 1).first()
    assert todo is None
    assert response.json() == {"detail": "Todo deleted successfully"}


def test_delete_todo_not_found(test_todo):
    response = client.delete("/todos/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}
