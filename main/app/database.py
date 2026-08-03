import os
import logging
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)

load_dotenv()

DATABASE_URL = (
    f"postgresql://"
    f"{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

logger.info(
    "Initializing database connection. Host: %s, Database: %s",
    os.getenv("POSTGRES_HOST"),
    os.getenv("POSTGRES_DB")
)

try:
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True
    )

    logger.info("Database engine created successfully")

except SQLAlchemyError:
    logger.exception("Failed to create database engine")
    raise

BASE_DIR = Path(__file__).resolve().parent.parent

def initialize_database():
    sql_file = BASE_DIR / "scripts" / "init_postgres_db.sql"

    with open(sql_file, "r", encoding="utf-8") as f:
        sql = f.read()

    with engine.begin() as conn:
        conn.execute(text(sql))

