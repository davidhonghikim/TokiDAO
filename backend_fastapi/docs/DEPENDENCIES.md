# Dependencies - TokiDAO FastAPI Backend

This file lists the primary dependencies of the project and their licenses, where known.
It complements `requirements.txt` by providing a place for notes on licensing or usage.

## Python Packages (from `requirements.txt`)

| Package          | Version (Initial) | License (Commonly) | Notes                                      |
|------------------|-------------------|--------------------|--------------------------------------------|
| fastapi          | >=0.100.0         | MIT                | Main web framework.                        |
| uvicorn          | latest            | BSD-3-Clause       | ASGI server (with `standard` extras).      |
| pymongo          | >=4.0             | Apache-2.0         | MongoDB driver.                            |
| python-dotenv    | latest            | BSD-3-Clause       | For loading `.env` files.                  |
| passlib[bcrypt]  | latest            | BSD                | Password hashing (bcrypt extra included).  |
| python-jose[cryptography] | latest    | MIT (python-jose), Multiple (cryptography) | JWT handling (cryptography extra included). |

*Note: Versions in `requirements.txt` will be the source of truth. "Latest" indicates the version at the time of initial setup or last update here. Licenses are typical; always verify if critical.*

## Other Tools / Services

| Tool/Service   | Usage                | Licensing/Cost Notes         |
|----------------|----------------------|------------------------------|
| MongoDB Atlas  | Cloud Database       | Free tier available (M0). Paid tiers for production. |
| Python         | Programming Language | Python Software Foundation License |
| Git            | Version Control      | GPLv2                        |

