from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone
import os

from .database import get_db, init_db
from .models import Trend, Content, AgentTask
from .schemas import TrendCreate, ContentCreate, TaskCreate
from .agent import run_agent_cycle

app = FastAPI(
    title="DesiGen AI",
    description="Indian Gen-Z social media AI agent",
    version="0.2.0",
)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {
        "app": "DesiGen AI",
        "status": "online",
        "version": "0.2.0",
        "message": "DesiGen AI backend is running",
    }

@app.get("/health")
def health(db: Session = Depends(get_db)):
    try:
        db.execute(__import__("sqlalchemy").text("SELECT 1"))
        database = "connected"
    except Exception:
        database = "error"
    return {
        "status": "healthy" if database == "connected" else "degraded",
        "database": database,
        "server_time": datetime.now(timezone.utc).isoformat(),
    }

@app.get("/api/status")
def api_status(db: Session = Depends(get_db)):
    return {
        "agent": "online",
        "database": "connected",
        "trend_engine": "ready",
        "content_engine": "ready",
        "instagram": "not_connected",
        "youtube": "not_connected",
    }

@app.post("/api/trends")
def create_trend(data: TrendCreate, db: Session = Depends(get_db)):
    trend = Trend(**data.model_dump())
    db.add(trend)
    db.commit()
    db.refresh(trend)
    return trend

@app.get("/api/trends")
def list_trends(db: Session = Depends(get_db)):
    return db.query(Trend).order_by(Trend.created_at.desc()).limit(100).all()

@app.post("/api/content")
def create_content(data: ContentCreate, db: Session = Depends(get_db)):
    item = Content(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@app.get("/api/content")
def list_content(db: Session = Depends(get_db)):
    return db.query(Content).order_by(Content.created_at.desc()).limit(100).all()

@app.post("/api/tasks")
def create_task(data: TaskCreate, db: Session = Depends(get_db)):
    task = AgentTask(**data.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@app.get("/api/tasks")
def list_tasks(db: Session = Depends(get_db)):
    return db.query(AgentTask).order_by(AgentTask.created_at.desc()).limit(100).all()

@app.post("/api/agent/run")
def agent_run(db: Session = Depends(get_db)):
    return run_agent_cycle(db)
