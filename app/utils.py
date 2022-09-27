from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


#compares plain text password against hashed one stored in db
def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)

