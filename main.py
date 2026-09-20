from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="DesiGen AI",
    description="Indian Gen-Z social media AI agent",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {
        "app": "DesiGen AI",
        "status": "online",
        "version": "0.1.0",
        "message": "DesiGen AI backend is running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "server_time": datetime.now(timezone.utc).isoformat()
    }


@app.get("/api/status")
async def api_status():
    return {
        "agent": "offline",
        "trend_engine": "not_started",
        "content_engine": "not_started",
        "instagram": "not_connected",
        "youtube": "not_connected"
    }
