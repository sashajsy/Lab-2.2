from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from models import metadata

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Використовуємо існуючі метадані з models.py
target_metadata = metadata

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True  # Додаємо цю опцію, щоб уникнути дублювання
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
