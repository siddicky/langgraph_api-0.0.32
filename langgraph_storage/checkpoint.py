"""Checkpoint dispatch layer.

Routes to either in-memory or Postgres backend based on DATABASE_URI.
"""

from langgraph_storage import USE_POSTGRES

if USE_POSTGRES:
    from langgraph_storage.postgres.checkpoint import Checkpointer  # noqa: F401
else:
    from langgraph_storage.inmem.checkpoint import (  # noqa: F401
        MEMORY,
        Checkpointer,
    )
