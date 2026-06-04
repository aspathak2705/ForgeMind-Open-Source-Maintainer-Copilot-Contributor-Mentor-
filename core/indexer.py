import json

from core.parser.file_scanner import FileScanner
from core.parser.python_parser import PythonParser
from storage.sqlite.database import Database

class RepositoryIndexer:

    def __init__(self):
        self.db = Database()

    def index(self, repo_path:str):

        files = FileScanner.scan_python_files(repo_path)

        for file in files:

            parsed = PythonParser.parse(file)

            self.db.conn.execute(
                """
                INSERT OR REPLACE INTO files
                (
                 path,
                 imports,
                 classes,
                 functions
                 )
                 VALUES (?, ?, ?, ?)
                """,
                (
                    parsed.path,
                    json.dumps(parsed.imports),
                    json.dumps(parsed.classes),
                    json.dumps(parsed.functions)
                )
            )

        self.db.conn.commit()

        return len(files)
    
