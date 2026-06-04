import os
import sqlite3
from pathlib import Path


def get_db_path():

    custom = os.getenv(
        "FORGEMIND_DB_PATH"
    )

    if custom:
        return Path(custom)

    return (
        Path.home()
        / ".forgemind"
        / "forgemind.db"
    )


class Database:

    def __init__(self, db_path: str | Path | None = None):
        resolved_path = Path(db_path).expanduser() if db_path else get_db_path()
        resolved_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(resolved_path))
        self.create_tables()

    def create_tables(self):

        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY,
            path TEXT UNIQUE,
            imports TEXT,
            classes TEXT,
            functions TEXT
        )
        """)

        self.conn.commit()
