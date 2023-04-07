from typing import Any
from fastapi import APIRouter, Depends
from app.db.base import get_db
from app.modules.auth.schemas.account_auth import AccountAuth
from app.modules.auth.services.authenticate_account import AuthenticateAccount
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["authentication"],
    responses={404: {"description": "not.found"}},
)


@router.post("/")
async def authenticate_account(
    account_form: AccountAuth, db: Session = Depends(get_db)
):
    authenticate_account_service = AuthenticateAccount(db)

    authenticated_token = authenticate_account_service.execute(account_form)

    return authenticated_token
