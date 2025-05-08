# TokiDAO Backend (FastAPI)

This directory contains the FastAPI backend for the TokiDAO project, part of the League of Orphans (LOO) initiative.

## Project Overview

TokiDAO is a gamified, blockchain-integrated plant and mushroom database and garden tracking platform. This backend will serve as the API for the Next.js frontend and handle business logic, database interactions (MongoDB Atlas), and future integrations.

## Setup

1.  **Prerequisites:**
    *   Python 3.8+
    *   pip
    *   A MongoDB Atlas account and cluster (or local MongoDB instance).

2.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables:**
    Create a `.env` file in this directory (`backend_fastapi`) with your MongoDB connection details:
    ```env
    MONGODB_URI=mongodb+srv://thedangerdawg:<YOUR_DB_PASSWORD>@cluster0.36zhlxw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
    # Replace <YOUR_DB_PASSWORD> with your actual MongoDB Atlas password.
    # For local MongoDB, it might look like: MONGODB_URI=mongodb://localhost:27017/tokidao_db
    
    SECRET_KEY=your_super_secret_random_key_for_jwt
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```
    **Important:** Replace `<YOUR_DB_PASSWORD>` with your actual password and generate a strong `SECRET_KEY` (e.g., using `openssl rand -hex 32`).

5.  **Run the Development Server:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will typically be available at `http://127.0.0.1:8000`.

## Project Structure (Initial)

```
backend_fastapi/
├── .env               # Local environment variables (MUST NOT be committed)
├── .gitignore         # Specifies intentionally untracked files that Git should ignore
├── main.py            # Main FastAPI application instance and root endpoints
├── requirements.txt   # Project dependencies
├── README.md          # This file
└── app/               # Application-specific modules
    ├── __init__.py
    ├── core/          # Core components like config, db connection
    │   ├── __init__.py
    │   └── config.py  # Configuration settings (e.g., env vars)
    │   └── db.py      # Database connection and utility functions
    ├── models/        # Pydantic models for data validation and serialization
    │   └── __init__.py
    ├── schemas/       # Pydantic schemas (similar to models, often used for API I/O)
    │   └── __init__.py
    └── api/           # API routers and endpoints
        ├── __init__.py
        └── v1/        # API version 1
            ├── __init__.py
            └── endpoints/ # Specific endpoint modules (e.g., plants, users)
                └── __init__.py
```

## Next Steps

*   Implement database connection logic in `app/core/db.py`.
*   Define Pydantic models in `app/models/` for plants, users, etc.
*   Create API endpoints in `app/api/v1/endpoints/`.
