import json

from core.services.repository_service import (
    RepositoryService,
)


class RepositoryHealth:

    def __init__(self):

        self.repo = (
            RepositoryService()
        )

    def analyze(self):

        files = (
            self.repo.get_all_files()
        )

        total_files = len(files)

        total_classes = 0
        total_functions = 0
        total_imports = 0

        for row in files:

            imports = json.loads(row[2])

            classes = json.loads(row[3])

            functions = json.loads(row[4])

            total_imports += len(imports)
            total_classes += len(classes)
            total_functions += len(functions)

        return {
            "total_files": total_files,
            "total_classes": total_classes,
            "total_functions": total_functions,
            "total_imports": total_imports,
        }