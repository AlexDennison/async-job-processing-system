from sqlalchemy.orm import Session
from app.core.job_status import JobStatus
from app.repositories import job_repository
from app.workers.job_worker import process_job


def submit_job(db: Session, job_type: str, payload: dict):

    job = job_repository.create_job(
        db=db,
        job_type=job_type,
        payload=payload,
        status=JobStatus.PENDING.value
    )

    process_job.delay(job.id)
    return job

def get_job_status(db: Session, job_id: str):
    return job_repository.get_job_by_id(db, job_id)
