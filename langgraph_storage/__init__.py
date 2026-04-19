"""LangGraph storage backends.

Selects between in-memory and Postgres+Redis backends based on DATABASE_URI.
"""

from os import getenv

USE_POSTGRES = getenv("DATABASE_URI") is not None or getenv("POSTGRES_URI") is not None
