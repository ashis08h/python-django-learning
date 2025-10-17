from passlib.context import CryptContext


pwd_crypt = CryptContext(schemes=["bcrypt"], deprecated='auto')


class Hash:

    def bcrypt(self, password: str):
        return pwd_crypt.hash(password)

    def verify(self, hashed_password, plain_password):
        return pwd_crypt.verify(plain_password, hashed_password)