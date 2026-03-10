from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.core.job_status import JobStatus
from app.models.job import Job
from app.schemas.job import JobCreate
from app.services import job_service

router = APIRouter()

@router.post("/jobs")
def submit_job(job: JobCreate, db: Session = Depends(get_db)):

    new_job = job_service.submit_job(
        db=db,
        job_type=job.type,
        payload=job.payload
    )

    return {
        "job_id": new_job.id,
        "status": new_job.status
    }

@router.get("/jobs/{job_id}")
def get_job(job_id: str, db: Session = Depends(get_db)):

    job = job_service.get_job_status(db, job_id)

    if not job:
        return {"error": "job not found"}

    return {
        "job_id": job.id,
        "status": job.status,
        "type": job.type
    }

