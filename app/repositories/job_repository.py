from sqlalchemy.orm import Session
from app.models.job import Job


def create_job(db: Session, job_type: str, payload: dict, status: str):
    job = Job(
        type=job_type,
        payload=payload,
        status=status
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job


def get_job_by_id(db: Session, job_id: str):
    return db.query(Job).filter(Job.id == job_id).first()
