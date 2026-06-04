import json
import sqlite3
from storage.sqlite.database import get_db_path


class RepositoryService:

    def __init__(self):
        db_path = get_db_path()
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(db_path))

    def get_all_files(self):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM files
            """
        )

        return cursor.fetchall()

    def get_summary(self):

        rows = self.get_all_files()

        total_files = len(rows)

        total_classes = 0
        total_functions = 0

        imports_frequency = {}

        for row in rows:

            imports = json.loads(row[2])
            classes = json.loads(row[3])
            functions = json.loads(row[4])

            total_classes += len(classes)
            total_functions += len(functions)

            for imp in imports:

                imports_frequency[imp] = (
                    imports_frequency.get(imp, 0)
                    + 1
                )

        most_imported = sorted(
            imports_frequency.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]

        return {
            "files": total_files,
            "classes": total_classes,
            "functions": total_functions,
            "most_imported": most_imported,
        }
