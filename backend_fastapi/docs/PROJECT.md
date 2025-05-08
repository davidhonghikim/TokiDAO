# Project Log: TokiDAO FastAPI Backend

This document tracks key decisions, frameworks, tools, and architectural choices for the TokiDAO FastAPI backend.

## 1. Overview
- **Project Name:** TokiDAO API
- **Description:** Backend API for the TokiDAO project - a gamified plant and mushroom database and garden tracking platform.
- **Primary Goal:** Provide a robust, scalable, and secure API for the TokiDAO frontend and potential future integrations.

## 2. Core Technologies & Frameworks
- **Language:** Python 3.11+
- **Framework:** FastAPI
- **Web Server:** Uvicorn
- **Database:** MongoDB (Atlas)
- **ODM/Driver:** Pymongo
- **Environment Management:** `python-dotenv`
- **Configuration:** Pydantic
- **Authentication (Planned):** JWT with Passlib for password hashing.

## 3. Directory Structure
(Refer to `README.md` for the main structure. Key decisions regarding internal `app` structure will be logged here.)

- `app/core/`: Core logic (config, DB connection).
- `app/models/`: Pydantic models representing database entities.
- `app/schemas/`: Pydantic schemas for API request/response validation and serialization.
- `app/api/v1/`: Version 1 of the API.
    - `app/api/v1/endpoints/`: Specific endpoint modules (e.g., `plants.py`, `users.py`).
    - `app/api/v1/api.py`: Aggregates all v1 routers.
- `app/crud/`: Functions for Create, Read, Update, Delete operations on database models.
- `app/services/`: Business logic layer (if needed, for more complex operations beyond simple CRUD).
- `app/utils/`: Utility functions.
- `app/tests/`: Unit and integration tests.

## 4. Key Decisions & Rationale
- **[Current Date] - Initial Setup:**
    - Chose FastAPI for its performance, ease of use, and automatic data validation & documentation.
    - Selected MongoDB Atlas for a scalable, managed NoSQL database solution, aligning with flexible data structures for plants/fungi.
    - Implemented basic environment variable management with `.env` and Pydantic settings.
- **[Current Date] - Project Tracking Files:**
    - Established `PROJECT.md`, `TODO.md`, `ISSUES.md`, `CHANGELOG.md`, `DEPENDENCIES.md` within a `logs` directory in `backend_fastapi` as per user rules.

## 5. Future Considerations / To Be Decided
- Detailed logging strategy (beyond basic console output).
- Background task management (e.g., Celery).
- Caching mechanisms.
- Rate limiting.
- CI/CD pipeline.
