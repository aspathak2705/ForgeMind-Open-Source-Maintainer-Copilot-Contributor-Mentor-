import sqlite3

from storage.sqlite.database import (
    get_db_path,
)


class GitHubRepository:

    def __init__(self):

        self.conn = sqlite3.connect(
            str(get_db_path())
        )

        self.create_tables()

    def create_tables(self):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS github_issues (
                id INTEGER PRIMARY KEY,
                issue_number INTEGER,
                title TEXT,
                body TEXT,
                state TEXT,
                labels TEXT
            )
            """
        )

        self.conn.commit()