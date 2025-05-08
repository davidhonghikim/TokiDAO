# Changelog - TokiDAO FastAPI Backend

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - YYYY-MM-DD
### Added
- Initial FastAPI project structure for TokiDAO backend.
- Core application setup (`main.py`).
- Environment variable management (`app/core/config.py`, `.env` file).
- MongoDB connection setup (`app/core/db.py`).
- Basic health check (`/health`) and root (`/`) endpoints.
- `requirements.txt` with initial dependencies (FastAPI, Uvicorn, Pymongo, python-dotenv, Passlib, python-jose).
- `.gitignore` file.
- `README.md` with project overview and setup instructions.
- Project tracking files in `logs/` directory:
    - `PROJECT.md`: Tracks key decisions, frameworks, and architecture.
    - `TODO.md`: Lists pending tasks and features.
    - `ISSUES.md`: Documents issues and their resolutions.
    - `CHANGELOG.md`: This file, for versioned changes.
    - `DEPENDENCIES.md`: For tracking libraries and licenses.

### Changed
- Integrated MongoDB connection into FastAPI startup/shutdown events in `main.py`.

### Fixed
- Corrected MongoDB authentication issue by ensuring the password in `.env` was accurate (removed erroneous angle brackets).
- Ensured `logs` directory is created before writing project tracking files into it.

