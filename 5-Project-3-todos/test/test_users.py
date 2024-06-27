from test.utils import *
from fastapi import status
from routers.users import get_db, get_current_user

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get("/user/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "user@test.com"
    assert response.json()["first_name"] == "Test"
    assert response.json()["last_name"] == "User"
    assert response.json()["role"] == "admin"
    assert response.json()["phone_number"] == "123456789"


def test_change_password_success(test_user):
    response = client.put(
        "/user/password",
        json={"password": "password", "new_password": "newpassword"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Password updated successfully"}


def test_change_invalid_current_password(test_user):
    response = client.put(
        "/user/password",
        json={"password": "invalidpassword", "new_password": "newpassword"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Error: Invalid password"}


def test_change_phone_number_success(test_user):
    response = client.put("/user/phonenumber/987654321")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Phone number updated successfully:"}
