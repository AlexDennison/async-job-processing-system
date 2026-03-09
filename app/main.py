from fastapi import APIRouter, FastAPI

from app.api import routes

app = FastAPI(title="Async Job Processing System")

app.include_router(routes.router)


@app.get("/health")
async def health_check():
    return {"status": "ok"}
