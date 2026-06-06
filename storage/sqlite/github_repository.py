import json
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
                issue_number INTEGER PRIMARY KEY,
                title TEXT,
                body TEXT,
                state TEXT,
                labels TEXT
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS github_pull_requests (
                pr_number INTEGER PRIMARY KEY,
                title TEXT,
                body TEXT,
                state TEXT
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS github_labels (
                name TEXT PRIMARY KEY,
                description TEXT
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS github_contributors (
                login TEXT PRIMARY KEY,
                contributions INTEGER
            )
            """
        )

        self.conn.commit()

    # --------------------
    # Issues
    # --------------------

    def save_issue(
        self,
        issue_number,
        title,
        body,
        state,
        labels,
    ):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            INSERT OR REPLACE INTO github_issues
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                issue_number,
                title,
                body,
                state,
                json.dumps(labels),
            ),
        )

        self.conn.commit()

    def get_issue(
        self,
        issue_number,
    ):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM github_issues
            WHERE issue_number = ?
            """,
            (issue_number,),
        )

        row = cursor.fetchone()

        if not row:
            return None

        return {
            "number": row[0],
            "title": row[1],
            "body": row[2],
            "state": row[3],
            "labels": json.loads(
                row[4]
            ),
        }

    def get_all_issues(self):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM github_issues
            """
        )

        return cursor.fetchall()