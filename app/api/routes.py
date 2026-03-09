from fastapi import APIRouter
from app.schemas.job import JobCreate
import uuid

router = APIRouter()

@router.post("/jobs")
async def submit_job(job: JobCreate):
    job_id = str(uuid.uuid4())

    return {
        "job_id": job_id,
        "status": "submitted"
    }
