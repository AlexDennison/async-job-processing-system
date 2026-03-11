import time
from app.core.celery_app import celery_app
from app.core.database import SessionLocal
from app.models.job import Job
from app.core.job_status import JobStatus


@celery_app.task
def process_job(job_id: str):

    db = SessionLocal()

    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        return

    job.status = JobStatus.PROCESSING.value
    db.commit()

    # simulate long running work
    time.sleep(10)

    job.status = JobStatus.SUCCESS.value
    db.commit()

    db.close()
