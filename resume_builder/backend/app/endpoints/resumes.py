from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..models.resume import Resume
from ..models.user import User
from ..database.session import get_db
from ..schemas.resume import ResumeCreate, ResumeOut

router = APIRouter()

@router.post("/", response_model=ResumeOut)
async def create_resume(resume: ResumeCreate, db: Session = Depends(get_db)):
    # Create new resume
    db_resume = Resume(
        title=resume.title,
        content=resume.content,
        user_id=resume.user_id
    )
    
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)
    
    return db_resume

@router.get("/{resume_id}", response_model=ResumeOut)
async def get_resume(resume_id: int, db: Session = Depends(get_db)):
    db_resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not db_resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found"
        )
    return db_resume

@router.get("/user/{user_id}", response_model=list[ResumeOut])
async def get_user_resumes(user_id: int, db: Session = Depends(get_db)):
    db_resumes = db.query(Resume).filter(Resume.user_id == user_id).all()
    return db_resumes