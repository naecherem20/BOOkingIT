import os
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
import jwt
from typing import Annotated
from pydantic import BaseModel
from sqlmodel import Session, select
from passlib.context import CryptContext
from  datetime import timedelta,datetime, timezone
from jwt.exceptions import InvalidTokenError,PyJWTError
from jose import JWTError,jwt
from database.connection import get_session
from models.user_model import User
from schema.user_login_schema import Token,TokenData
from dotenv import load_dotenv
import uuid
load_dotenv()




SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login", scheme_name="user")

pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], session: Session =  Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user_id = uuid.UUID(username)
    user = session.exec(select(User).where(User.id == user_id)).first()    
    if user is None:
        raise credentials_exception
    return user

