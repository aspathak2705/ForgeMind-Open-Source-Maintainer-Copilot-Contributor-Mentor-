import json

from storage.sqlite.database import (
    Database,
)


class MemoryStore:

    def __init__(self):

        self.db = Database()

    def add(
        self,
        record: dict,
    ):

        cursor = self.db.conn.cursor()

        cursor.execute(
            """
            INSERT INTO agent_memory
            (
                agent,
                task,
                result
            )
            VALUES (?, ?, ?)
            """,
            (
                record["agent"],
                record["task"],
                json.dumps(
                    record["result"]
                ),
            ),
        )

        self.db.conn.commit()

    def get_all(self):

        cursor = self.db.conn.cursor()

        cursor.execute(
            """
            SELECT
                id,
                agent,
                task,
                result,
                created_at
            FROM agent_memory
            ORDER BY id DESC
            """
        )

        return cursor.fetchall()

    def count(self):

        cursor = self.db.conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM agent_memory
            """
        )

        return cursor.fetchone()[0]