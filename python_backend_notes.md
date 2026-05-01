# Python Backend Notes (FastAPI + Pydantic + SQLAlchemy)

## 1) Big Picture
- `FastAPI`: used to build APIs (routes like `GET`, `POST`, etc.)
- `Pydantic`: validates request/response data using Python classes
- `SQLAlchemy`: talks to the database using Python models and sessions
- Flow: `Client -> FastAPI route -> Pydantic validation -> business logic -> DB (SQLAlchemy) -> response`

## 2) FastAPI Basics
- Route decorators:
  - `@app.get("/users")`
  - `@app.post("/users")`
  - `@app.put("/users/{id}")`
  - `@app.delete("/users/{id}")`
- Path param:
  - `"/users/{user_id}"` and function arg `user_id: int`
- Query param:
  - `"/users?limit=10"` -> function arg `limit: int = 10`
- Status code:
  - create endpoint usually returns `201`
- Error handling:
  - `raise HTTPException(status_code=404, detail="User not found")`

## 3) Pydantic Essentials
- Use `BaseModel` for schemas.
- Use `Field(...)` for constraints:
  - `gt`, `ge`, `lt`, `le`
  - `min_length`, `max_length`
- Use proper types:
  - `EmailStr` for email
  - `str | None = None` for optional values
- Useful methods:
  - `model_dump()` -> convert model to dictionary

## 4) Common Beginner Mistakes (and fixes)
- **Wrong route string**
  - Mistake: `@app.get(f"/users/{user_id}")`
  - Fix: `@app.get("/users/{user_id}")`
- **Missing imports**
  - If using `HTTPException`, import it from `fastapi`.
- **Schema name mismatch**
  - Keep model names and type hints consistent (`User` vs `Users`).
- **No duplicate checks**
  - Before create, check existing IDs/emails.
- **Unreachable code**
  - Remove code after a guaranteed `return`.

## 5) SQLAlchemy Basics (starter)
- `engine`: DB connection
- `SessionLocal`: database session factory
- `Base`: parent class for table models
- Table model example fields:
  - `id`, `name`, `email`, `age`
- Basic CRUD shape:
  - Create -> add + commit + refresh
  - Read -> query/filter/first/all
  - Update -> load row, modify, commit
  - Delete -> load row, delete, commit

## 6) Recommended Project Structure (when ready)
- `main.py` (app + routers)
- `models.py` (SQLAlchemy models)
- `schemas.py` (Pydantic request/response models)
- `database.py` (engine/session/base)
- `crud.py` (DB operations)

## 7) API Testing Checklist
- Open `/docs` and test every endpoint.
- Test valid + invalid payloads.
- Confirm status codes are correct (`200`, `201`, `400`, `404`, `422`).
- Confirm duplicate create is blocked.
- Confirm not-found handling works.

## 8) Daily Learning Template (copy daily)
```md
# Day XX - Topic

## Goal

## What I Built

## What I Learned

## Errors I Faced
- Error:
- Why it happened:
- Fix:

## Endpoints Practiced
- GET
- POST
- PUT
- DELETE

## Tomorrow Plan
```

## 9) Practical Advice
- Build small, run often.
- Keep one concept per day.
- Write one bug + fix daily (best learning booster).
- Do not jump to auth/deployment too early.
