

from fastapi.security import OAuth2PasswordRequestForm
from app.modules.auth.schemas.account import Account


def test_authenticate_account_success(client, account: Account):
    response = client.post(
        '/auth/', json={
            "username": account.username,
            "password": "12345678"
        }
    )

    assert response.status_code == 200
