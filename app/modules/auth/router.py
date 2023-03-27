from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from app.db.base import get_db
from app.modules.auth.schemas.account import AccountAuth
from app.modules.auth.services.authenticate_account import AuthenticateAccount
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/auth",
    tags=["authentication"],
    responses={404: {"description": "not.found"}},
)


@router.post("/")
async def authenticate_account(account: AccountAuth, db: Session = Depends(get_db)):
    authenticate_account_service = AuthenticateAccount(db)

    authenticated_token = authenticate_account_service.execute(account)

    return authenticated_token
