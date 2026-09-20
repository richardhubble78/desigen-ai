# DesiGen AI

DesiGen AI is an Indian Gen-Z focused agentic social-media manager backend.

## Current architecture

- FastAPI API
- PostgreSQL persistence
- Trend storage
- Content drafts
- Agent task tracking
- Agent cycle endpoint
- Health/status endpoints
- Render deployment configuration

## Local run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `/docs` for the API interface.

## Render

Set the `DATABASE_URL` environment variable on the web service to the PostgreSQL **Internal Database URL** from the Render database in the same region.

Do not commit database passwords or API keys.

## Agent roadmap

1. Persistent database and memory
2. LLM content generation
3. Trend ingestion
4. Content scoring
5. Instagram/YouTube OAuth
6. Scheduling
7. Analytics
8. Approval/autopilot modes
9. Multi-agent orchestration
