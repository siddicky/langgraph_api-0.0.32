"""Database connection dispatch layer.

Routes to either in-memory or Postgres backend based on DATABASE_URI.
"""

from langgraph_storage import USE_POSTGRES

if USE_POSTGRES:
    from langgraph_storage.postgres.database import (  # noqa: F401
        connect,
        get_pool,
        healthcheck,
        pool_stats,
        start_pool,
        stop_pool,
    )
else:
    from langgraph_storage.inmem.database import (  # noqa: F401
        InMemConnectionProto,
        connect,
        healthcheck,
        pool_stats,
        start_pool,
        stop_pool,
    )
