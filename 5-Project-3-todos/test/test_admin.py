from test.utils import *
from fastapi import status
from routers.admin import get_db, get_current_user
from fastapi import status
from models import Todos

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_read_all_authenticated(test_todo):
    response = client.get("/admin/todos")
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


def test_admin_delete_todo(test_todo):
    response = client.delete("/admin/todos/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Todo deleted successfully"}
    db = TestingSessionLocal()
    todo = db.query(Todos).filter(Todos.id == 1).first()
    assert todo is None
    db.close()


def test_admin_delete_todo_not_found(test_todo):
    response = client.delete("/admin/todos/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}
