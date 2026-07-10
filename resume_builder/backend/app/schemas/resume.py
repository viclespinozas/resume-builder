from pydantic import BaseModel
from typing import Optional

class ResumeBase(BaseModel):
    title: str
    content: Optional[str] = None
    user_id: int

class ResumeCreate(ResumeBase):
    pass

class ResumeOut(ResumeBase):
    id: int
    
    class Config:
        orm_mode = True