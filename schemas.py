from pydantic import BaseModel, Field
from typing import Any, Dict

class TrendCreate(BaseModel):
    topic: str = Field(min_length=1, max_length=255)
    platform: str = "general"
    score: float = 0
    source: str = "manual"
    metadata_json: Dict[str, Any] = {}

class ContentCreate(BaseModel):
    title: str
    body: str
    platform: str = "instagram"
    status: str = "draft"
    content_type: str = "post"

class TaskCreate(BaseModel):
    task_type: str
    input_json: Dict[str, Any] = {}
