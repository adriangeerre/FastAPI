from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "8ed62bfc9695daa60657c2ac415f716838b4bef5d48a3feed0ed26ac188d60e2"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    enconded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return enconded_jwt