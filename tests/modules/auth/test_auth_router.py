

from fastapi.security import OAuth2PasswordRequestForm
from app.modules.auth.schemas.account import Account
import pytest
from async_asgi_testclient import TestClient


@pytest.mark.asyncio
async def test_authenticate_account_success(client: TestClient, account: Account):
    response = await client.post(
        '/auth/', json={
            "username": account.username,
            "password": "12345678"
        }
    )

    assert response.status_code == 200
