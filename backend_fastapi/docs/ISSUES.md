# TokiDAO API - Issues & Resolutions

This document tracks significant issues encountered during development and their resolutions.

| Date       | Issue ID / Description                                  | Affected Area(s) | Reporter | Status      | Resolution / Notes                                                                                                |
|------------|---------------------------------------------------------|------------------|----------|-------------|-------------------------------------------------------------------------------------------------------------------|
| YYYY-MM-DD | Initial MongoDB Connection Failure                      | `db.py`, `main.py` | System   | Resolved    | **Error:** `pymongo.errors.OperationFailure: bad auth : authentication failed`                                    |
|            |                                                         |                  |          |             | **Cause:** Incorrect password in `.env` (included `<` and `>`).                                                   |
|            |                                                         |                  |          |             | **Resolution:** Corrected the `MONGODB_URI` password string in the `.env` file by removing the angle brackets. |
| YYYY-MM-DD | Attempt to write to non-existent `logs` directory     | File Generation  | Cascade  | Resolved    | **Error:** `open ... no such file or directory` when trying to create `PROJECT.md`.                             |
|            |                                                         |                  |          |             | **Cause:** `logs` directory was not created before attempting to write a file into it.                            |
|            |                                                         |                  |          |             | **Resolution:** Added a step to explicitly create the `logs` directory using `mkdir -p` before writing files. |
|            |                                                         |                  |          |             |                                                                                                                   |
