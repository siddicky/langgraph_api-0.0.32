"""LangGraph storage backends.

Selects between in-memory and Postgres+Redis backends based on DATABASE_URI.
"""

from os import getenv

USE_POSTGRES = bool(
    (getenv("DATABASE_URI") and getenv("DATABASE_URI").strip())
    or (getenv("POSTGRES_URI") and getenv("POSTGRES_URI").strip())
)
