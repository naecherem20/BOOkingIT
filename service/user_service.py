import os
from fastapi import APIRouter, HTTPException, Depends, status
from sqlmodel import Session, select
from fastapi.security import OAuth2PasswordRequestForm
from schema.user_schema import UserCreate,UserReturn
from passlib.context import CryptContext
from typing import Annotated
from models.user_model import User
from auth_config.user_login_auth import create_access_token,verify_password


pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")
class UserService:
    def __init__(self, session: Session):
        self.session = session

    def Register(self,user:UserCreate ):
        existing_user=self.session.exec(select(User).where(User.email==user.email)).first()
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

        hashed_password = pwd_context.hash(user.password)
        new_user = User(
            name=user.name,
            email=user.email,
            password=hashed_password,
            role=user.role,
            created_at=user.created_at,
        )
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user
    
    def login(self, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
        user = self.session.exec(select(User).where(User.email == form_data.username)).first()
        if not user or not verify_password(form_data.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid username or password")

        token = create_access_token({"sub": str(user.id), "role": "user"})
        return {"access_token": token, "token_type": "bearer"}