from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.core.job_status import JobStatus
from app.models.job import Job
from app.schemas.job import JobCreate

router = APIRouter()

@router.post("/jobs")
def submit_job(job: JobCreate, db: Session = Depends(get_db)):

    db_job = Job(
        type=job.type,
        payload=job.payload,
        status=JobStatus.PENDING.value
    )

    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    return {
        "job_id": db_job.id,
        "status": db_job.status
    }

@router.get("/jobs/{job_id}")
def get_job(job_id: str, db: Session = Depends(get_db)):

    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        return {"error": "job not found"}

    return {
        "job_id": job.id,
        "status": job.status,
        "type": job.type
    }

