from models.user_model import Service
from sqlmodel import Session, select
from schema.service_schema import Services
from uuid import UUID

class UserCRUDService:
    def __init__(self, session: Session):
        self.session = session

    def create_book(self, book_in:Services, user_id:UUID ):
        new_book = Service(**book_in.model_dump(),booking_id=user_id)
        self.session.add(new_book)
        self.session.commit()
        self.session.refresh(new_book)
        return new_book
    def get_all_booked_by_user(self, user_id:UUID | None = None):
        if user_id:
            book=self.session.exec(select(Service).where(Service.booking_id==user_id)).all()
            return book
        return []


