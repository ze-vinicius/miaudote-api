from databases import Database
from fastapi import APIRouter, Depends

from app.core.database import get_db
from app.modules.auth.schemas.account_auth import AccountAuth
from app.modules.auth.services.authenticate_account import AuthenticateAccount

router = APIRouter(
    prefix="/auth",
    tags=["authentication"],
    responses={404: {"description": "not.found"}},
)


@router.post("/")
async def authenticate_account(
    account_form: AccountAuth, db: Database = Depends(get_db)
):
    authenticate_account_service = AuthenticateAccount(db)

    authenticated_token = await authenticate_account_service.execute(account_form)

    return authenticated_token
