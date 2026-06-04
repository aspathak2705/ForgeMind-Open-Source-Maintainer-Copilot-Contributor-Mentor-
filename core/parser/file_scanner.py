from pathlib import Path

class FileScanner:

    EXCLUDED_DIRS = {
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        "node_modules",
        ".idea",
        ".vscode"
    }

    @classmethod
    def scan_python_files(cls,root: str)-> list[Path]:

        root_path = Path(root)

        files = []

        for file in root_path.rglob("*.py"):
            if any(part in cls.EXCLUDED_DIRS for part in file.parts):
                continue

            files.append(file)

        return files
    
    