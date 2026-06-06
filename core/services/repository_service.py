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
    
    def get_summary(self):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT
                imports,
                classes,
                functions
            FROM files
            """
        )

        rows = cursor.fetchall()

        total_files = len(rows)

        total_classes = 0
        total_functions = 0

        import_counter = {}

        for (
            imports,
            classes,
            functions,
        ) in rows:

            class_list = [
                item.strip()
                for item in (
                    classes or ""
                ).split(",")
                if item.strip()
            ]

            function_list = [
                item.strip()
                for item in (
                    functions or ""
                ).split(",")
                if item.strip()
            ]

            import_list = [
                item.strip()
                for item in (
                    imports or ""
                ).split(",")
                if item.strip()
            ]

            total_classes += len(
                class_list
            )

            total_functions += len(
                function_list
            )

            for module in import_list:

                import_counter[
                    module
                ] = (
                    import_counter.get(
                        module,
                        0,
                    )
                    + 1
                )

        most_imported = sorted(
            import_counter.items(),
            key=lambda x: x[1],
            reverse=True,
        )[:10]

        return {
            "files": total_files,
            "classes": total_classes,
            "functions": total_functions,
            "most_imported": most_imported,
        }