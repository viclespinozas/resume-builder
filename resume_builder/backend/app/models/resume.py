from sqlalchemy import Column, Integer, String, Text, ForeignKey, relationship
from .base import BaseModel
from ..models.user import User

class Resume(BaseModel):
    __tablename__ = "resumes"
    
    title = Column(String(255), nullable=False)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relationship
    user = relationship("User", back_populates="resumes")
