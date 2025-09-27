import os
from fastapi import APIRouter, HTTPException, Depends, status
from dotenv import load_dotenv
from sqlmodel import Session, select
from fastapi.security import OAuth2PasswordRequestForm
from database.connection import get_session
from schema.user_schema import UserCreate,UserReturn
from passlib.context import CryptContext
from typing import Annotated
from models.user_model import User
from auth_config.user_login_auth import create_access_token,get_current_user,verify_password
from service.user_service import UserService


load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL")
router=APIRouter(prefix="/auth",tags=["authentication"])
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register",response_model=UserReturn,status_code=status.HTTP_201_CREATED)
def Register(user:UserCreate, session:Session = Depends(get_session)):
    register=UserService(session)
    return register.Register(user)
 
@router.post("/login", status_code=status.HTTP_202_ACCEPTED)
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: Session = Depends(get_session)):
    user_login=UserService(session)
    return user_login.login(form_data)
@router.get("/me")
def get_me(current_user: Annotated[User, Depends(get_current_user)]):
    return {"id": current_user.id, "username": current_user.email,"message":"you've been logged in!!"}
    
