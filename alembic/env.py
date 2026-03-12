from logging.config import fileConfig
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from sqlalchemy.pool import NullPool
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from alembic import context

from app.database import Base
from app.config import DATABASE_URL  
from app import models  # importo tutti i modelli per far funzionare l'autogenerate

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Esegue le migration in 'offline' mode (senza connessione al DB)."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,    
        render_as_batch=True  
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Esegue le migration in 'online' mode (connessione diretta al DB)."""
   
    connectable = create_engine(DATABASE_URL, poolclass=NullPool)

    with connectable.connect() as connection:  
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,    
            render_as_batch=True  
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()