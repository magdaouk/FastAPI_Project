from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel


class Items(BaseModel):
    CurrentDestinationBarcode : str


# Define the compound_addition_ver2_0 table model
class CompoundAdditionVer2_0(Base):
    __tablename__ = "compound_addition_ver2_0"

    id = Column(Integer, primary_key=True, index=True)
    CurrentDestinationBarcode = Column(String)