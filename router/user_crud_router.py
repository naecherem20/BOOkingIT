from fastapi import APIRouter, Depends,status,HTTPException
from crud.user_crud import UserCRUDService
from sqlmodel import Session
from database.connection import get_session
from schema.service_schema import Services
from auth_config.user_login_auth import get_current_user
from uuid import UUID



router=APIRouter(prefix="/books", tags=["bookings"])

@router.post("/", response_model=Services,status_code=201)
def create_book(book_in:Services, session: Session=Depends(get_session), current_user=Depends(get_current_user)):
   service= UserCRUDService(session)
   return service.create_book(book_in, current_user.id)

@router.get("/")
def get_all_booked_by_user(session:Session=Depends(get_session),current_user=Depends(get_current_user)):
   service=UserCRUDService(session)
   return service.get_all_booked_by_user(current_user.id)

@router.delete("/", status_code=status.HTTP_404_NOT_FOUND)
def delete_book(book_id:UUID, session:Session=Depends(get_session), current_user=Depends(get_current_user)):
   service=UserCRUDService(session)
   return service.delete_book(book_id, current_user.id)