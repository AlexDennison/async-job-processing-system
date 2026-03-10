from sqlalchemy import Column, String, JSON, DateTime
from sqlalchemy.sql import func
from app.core.database import Base
from app.core.job_status import JobStatus
import uuid


class Job(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    type = Column(String, nullable=False)
    payload = Column(JSON, nullable=False)
    status = Column(String, index=True, default=JobStatus.PENDING.value)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
