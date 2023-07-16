from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlmodel import Session

from db import init_db, get_session
from models.manufactures_model import Manufactures, ManufacturesCreate

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
async def root():
    return {"message": "Hello World are sucks, veru sucks"}

@app.get("/manufactures", response_model=list[Manufactures])
def get_manufactures(session: Session = Depends(get_session)):
    result = session.execute(select(Manufactures))
    manufactures = result.scalars().all()
    return [Manufactures(id=manufacture.id, name=manufacture.name) for manufacture in manufactures]


@app.post("/manufactures")
async def add_manufacture(manufacture: ManufacturesCreate, session: Session = Depends(get_session)):
    check_name = session.execute(select(Manufactures).where(Manufactures.name == manufacture.name)).first()
    if check_name:
        raise HTTPException(status_code=400, detail="Name already exists")
    manufacture = Manufactures(name=manufacture.name)
    session.add(manufacture)
    session.commit()
    session.refresh(manufacture)
    return manufacture
