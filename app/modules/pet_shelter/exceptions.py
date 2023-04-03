from app.modules.pet_shelter.constants import ErrorCode
from app.core.exceptions import BadRequest, NotFound

class NotFound(BadRequest):
    DETAIL = ErrorCode.NOT_FOUND


class AlreadyExists(BadRequest):
    DETAIL = ErrorCode.PET_SHELTER_ALREADY_EXISTS

class AccountNotCreated(BadRequest):
    DETAIL = ErrorCode.ACCOUNT_NOT_CREATED

class PetShelterNotFound(NotFound):
    DETAIL = ErrorCode.PET_SHELTER_ALREADY_EXISTS

class PetNotFound(NotFound):
    DETAIL = ErrorCode.PET_NOT_FOUND