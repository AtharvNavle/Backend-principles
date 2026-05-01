# 18-Day Learning Schedule (FastAPI + Pydantic + SQLAlchemy)

This plan fits your 15-20 day target.  
Daily target: 60-120 minutes.

## Daily Rule (same every day)
- 10 min: revise yesterday
- 40-80 min: code today's topic
- 15 min: test in `/docs`
- 10 min: write your day file notes

## Day-by-Day Plan

### Day 1
- FastAPI setup, first `GET /`
- Understand `uvicorn`, reload, docs endpoint

### Day 2
- Pydantic validations (`Field`, `EmailStr`)
- `POST /users`, `GET /users`, `GET /users/{id}`
- Error handling with `HTTPException`

### Day 3
- Path params vs query params
- Add filters like `/users?min_age=20`

### Day 4
- Response models and status codes
- Return clean responses using `response_model`

### Day 5
- `PUT` update endpoint
- Partial update idea (basic understanding)

### Day 6
- `DELETE` endpoint
- Not-found and edge-case handling

### Day 7
- Mini revision day
- Build simple in-memory CRUD from scratch without notes

### Day 8
- SQLAlchemy intro: install + DB connection (`SQLite`)
- `engine`, `SessionLocal`, `Base`

### Day 9
- Create SQLAlchemy `User` table model
- Create tables and inspect DB rows

### Day 10
- Insert users into DB using session
- Replace in-memory list with DB create/read

### Day 11
- Read operations from DB:
  - list users
  - get by id
  - filters

### Day 12
- Update and delete in DB
- Proper commit/rollback basics

### Day 13
- Separate files:
  - `database.py`
  - `models.py`
  - `schemas.py`
  - `main.py`

### Day 14
- Add `crud.py` helper functions
- Keep routes thinner, move DB logic out

### Day 15
- Validation deep dive:
  - stricter constraints
  - better error messages

### Day 16
- Add second entity (example: `Song` or `Playlist`)
- Relationship basics (one-to-many concept)

### Day 17
- End-to-end mini project build day
- User + Song CRUD with clean structure

### Day 18
- Final revision and refactor day
- Clean naming, comments, endpoint consistency
- Prepare next phase plan (Auth + Alembic + Testing)

## If You Need a 15-Day Version
- Merge Day 7 into Day 6
- Merge Day 14 into Day 13
- Merge Day 18 into Day 17

## Daily Deliverable Rule
Create one file per day in this style:
- `day_01_...py`
- `day_02_...py`
- ...

And one note section at bottom:
- What I learned
- Errors and fixes
- 1 improvement for tomorrow
