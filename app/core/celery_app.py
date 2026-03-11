from celery import Celery

celery_app = Celery(
    "job_worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery_app.conf.task_routes = {
    "app.workers.job_worker.process_job": {"queue": "jobs"}
}
