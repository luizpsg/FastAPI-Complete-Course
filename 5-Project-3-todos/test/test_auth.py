from test.utils import *
from fastapi import status
from routers.auth import (
    get_db,
    authenticate_user,
    create_access_token,
    SECRET_KEY,
    ALGORITHM,
)
from jose import jwt
from datetime import datetime, timedelta

app.dependency_overrides[get_db] = override_get_db


def test_authenticate_user(test_user):
    db = TestingSessionLocal()

    authenticated_user = authenticate_user(db, test_user.username, "password")
    assert authenticated_user is not None
    assert authenticated_user.username == test_user.username

    non_existent_user = authenticate_user(db, "nonexistent", "password")
    assert non_existent_user is False

    wrong_password = authenticate_user(db, test_user.username, "wrongpassword")
    assert wrong_password is False
    db.close()


def test_create_access_token():
    username = "testuser"
    user_id = 1
    role = "user"
    expires_delta = timedelta(days=1)

    token = create_access_token(username, user_id, role, expires_delta)

    decoded_token = jwt.decode(
        token, SECRET_KEY, algorithms=[ALGORITHM], options={"verify_signature": False}
    )

    assert decoded_token.get("sub") == username
    assert decoded_token.get("id") == user_id
    assert decoded_token.get("role") == role
