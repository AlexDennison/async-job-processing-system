from fastapi import FastAPI

app = FastAPI(title="Async Job Processing System")


@app.get("/health")
async def health_check():
    return {"status": "ok"}
