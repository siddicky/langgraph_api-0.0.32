"""Store dispatch layer.

Routes to either in-memory or Postgres backend based on DATABASE_URI.
"""

from langgraph_storage import USE_POSTGRES

if USE_POSTGRES:
    from langgraph_storage.postgres.store import (  # noqa: F401
        Store,
        set_store_config,
        setup_vector_index,
    )
else:
    from langgraph_storage.inmem.store import (  # noqa: F401
        STORE,
        BatchedStore,
        DiskBackedInMemStore,
        Store,
        set_store_config,
    )
