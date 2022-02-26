from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel

class User(BaseModel, Base):
    __tablename__ = 'user'
    name = Column(String(60), nullable=False)
    password = Column(String(128), nullable=False)
