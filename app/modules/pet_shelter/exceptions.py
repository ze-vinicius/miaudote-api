from app.core.exceptions import BadRequest, NotFound
from app.modules.pet_shelter.constants import ErrorCode


class PetShelterAlreadyExists(BadRequest):
    DETAIL = ErrorCode.PET_SHELTER_ALREADY_EXISTS


class AccountNotCreated(BadRequest):
    DETAIL = ErrorCode.ACCOUNT_NOT_CREATED


class PetShelterNotFound(NotFound):
    DETAIL = ErrorCode.PET_SHELTER_NOT_FOUND


class PetNotFound(NotFound):
    DETAIL = ErrorCode.PET_NOT_FOUND
