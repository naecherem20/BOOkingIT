from fastapi import FastAPI
from sqlmodel import SQLModel
from database.connection import engine
from router.user_router import router as user_router
from router.user_crud_router import router as user_crud_router


app=FastAPI()
app.include_router(user_router)
app.include_router(user_crud_router)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
