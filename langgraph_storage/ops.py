"""Storage operations dispatch layer.

Routes to either in-memory or Postgres backend based on DATABASE_URI.
"""

from langgraph_storage import USE_POSTGRES

if USE_POSTGRES:
    from langgraph_storage.postgres.ops import *  # noqa: F401, F403
else:
    from langgraph_storage.inmem.ops import *  # noqa: F401, F403
