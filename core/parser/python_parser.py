import ast
from pathlib import Path

from core.models.file_node import FileNode


class PythonParser:

    @staticmethod
    def parse(file_path: Path)-> FileNode:

        source = file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        tree = ast.parse(source)

        imports=[]
        classes = []
        functions = []

        for node in ast.walk(tree):

            if isinstance(node,ast.Import):
                for alias in node.names:
                    imports.append(alias.name)

            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)
            
            elif isinstance(node, ast.ClassDef):
                classes.append(node.name)

            elif isinstance(node, ast.FunctionDef):
                functions.append(node.name)

        return FileNode(
            path = str(file_path),
            imports=imports,
            classes = classes,
            functions = functions
        )
