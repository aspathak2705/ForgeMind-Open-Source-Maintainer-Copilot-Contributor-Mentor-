import sqlite3

from storage.sqlite.database import (
    get_db_path,
)


class RepositoryService:

    def __init__(self):

        self.conn = sqlite3.connect(
            str(get_db_path())
        )

    def get_all_files(self):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT
                id,
                path,
                imports,
                classes,
                functions
            FROM files
            """
        )

        return cursor.fetchall()

    def search_files(
        self,
        query: str,
    ):

        cursor = self.conn.cursor()

        pattern = f"%{query}%"

        cursor.execute(
            """
            SELECT
                id,
                path,
                imports,
                classes,
                functions
            FROM files
            WHERE
                path LIKE ?
                OR imports LIKE ?
                OR classes LIKE ?
                OR functions LIKE ?
            """,
            (
                pattern,
                pattern,
                pattern,
                pattern,
            ),
        )

        return cursor.fetchall()

    def count_files(self):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM files
            """
        )

        return cursor.fetchone()[0]