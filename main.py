from enum import Enum
import random
import string
import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Base, SessionLocal, engine
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import models
from models import Items, CompoundAdditionVer2_0

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.post("/items/")
async def create_item(item: Items, db: Session = Depends(get_db)):
    try:
        db_item = CompoundAdditionVer2_0(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return "yes"
    except Exception as e:
        db.rollback()  # Rollback changes if an error occurs
        return f"Error creating item: {str(e)}"
    finally:
        db.close()  # Close the database session
 
# if __name__ == "__main__":
#     uvicorn.run(app, host="10.240.50.6", port=1900)
