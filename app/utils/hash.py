from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes="bcrypt", deprecated="auto")


class Hash:
    @classmethod
    def encrypt(cls, password: str):
        return pwd_cxt.hash(password)

    @classmethod
    def verify(cls, hashed_password: str, plain_password: str):
        return pwd_cxt.verify(plain_password, hashed_password)
