from datetime import datetime, timezone
from .models import AgentTask, Trend, Content

def generate_content(topic: str, platform: str = "instagram"):
    # Deterministic starter engine. Replace with an LLM provider later.
    hooks = [
        f"POV: you just discovered the real story behind {topic} 👀",
        f"Everyone is talking about {topic}. Here's what actually matters.",
        f"{topic} explained in 30 seconds — desi edition 🇮🇳",
    ]
    body = (
        f"{hooks[0]}\n\n"
        f"Key points:\n"
        f"• Why {topic} is getting attention\n"
        f"• What creators should know\n"
        f"• One practical takeaway\n\n"
        f"#India #GenZ #Trending"
    )
    return {"title": topic, "body": body, "platform": platform}

def run_agent_cycle(db):
    task = AgentTask(
        task_type="agent_cycle",
        status="running",
        input_json={"started_at": datetime.now(timezone.utc).isoformat()},
    )
    db.add(task)
    db.commit()
    db.refresh(task)

    trend = db.query(Trend).order_by(Trend.score.desc(), Trend.created_at.desc()).first()

    if trend:
        generated = generate_content(trend.topic)
        content = Content(
            title=generated["title"],
            body=generated["body"],
            platform=generated["platform"],
            status="draft",
            content_type="post",
        )
        db.add(content)
        result = {
            "selected_trend": trend.topic,
            "content_id": None,
            "action": "draft_created",
        }
    else:
        result = {
            "selected_trend": None,
            "action": "no_trends_available",
            "message": "Add a trend first.",
        }

    task.status = "completed"
    task.output_json = result
    task.completed_at = datetime.now(timezone.utc)
    db.commit()

    if trend:
        db.refresh(content)
        result["content_id"] = content.id

    return result
