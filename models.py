from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, JSON
from .database import Base

def now():
    return datetime.now(timezone.utc)

class Trend(Base):
    __tablename__ = "trends"
    id = Column(Integer, primary_key=True)
    topic = Column(String(255), nullable=False)
    platform = Column(String(50), default="general")
    score = Column(Float, default=0)
    source = Column(String(255), default="manual")
    metadata_json = Column(JSON, default=dict)
    created_at = Column(DateTime(timezone=True), default=now)

class Content(Base):
    __tablename__ = "content"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    platform = Column(String(50), default="instagram")
    status = Column(String(50), default="draft")
    content_type = Column(String(50), default="post")
    created_at = Column(DateTime(timezone=True), default=now)

class AgentTask(Base):
    __tablename__ = "agent_tasks"
    id = Column(Integer, primary_key=True)
    task_type = Column(String(100), nullable=False)
    status = Column(String(50), default="pending")
    input_json = Column(JSON, default=dict)
    output_json = Column(JSON, default=dict)
    created_at = Column(DateTime(timezone=True), default=now)
    completed_at = Column(DateTime(timezone=True), nullable=True)

class AgentMemory(Base):
    __tablename__ = "agent_memory"
    id = Column(Integer, primary_key=True)
    key = Column(String(255), nullable=False, index=True)
    value = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=now)
    updated_at = Column(DateTime(timezone=True), default=now, onupdate=now)
