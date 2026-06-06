import json

from storage.sqlite.database import (
    Database,
)


class ReflectionStore:

    def __init__(self):

        self.db = Database()

    def add(
        self,
        reflection: dict,
    ):

        cursor = self.db.conn.cursor()

        cursor.execute(
            """
            INSERT INTO reflections
            (
                agent,
                observation,
                metadata
            )
            VALUES (?, ?, ?)
            """,
            (
                reflection["agent"],
                reflection["observation"],
                json.dumps(
                    reflection["metadata"]
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
                observation,
                metadata,
                created_at
            FROM reflections
            ORDER BY id DESC
            """
        )

        return cursor.fetchall()