from passlib.context import CryptContext

my_hasher = CryptContext(schemes=["bcrypt"], deprecated = "auto")
#my_hasher is the hash object we created using the cryptcontext class
#bcrypt hashing algorithm used here
# deprecated="auto" allows Passlib to detect older
# hashing algorithms and migrate them if needed.

def hash_password(password):
    return  my_hasher.hash(password)

def verify_password(plain_password, hashed_password):
    return my_hasher.verify(plain_password,hashed_password)