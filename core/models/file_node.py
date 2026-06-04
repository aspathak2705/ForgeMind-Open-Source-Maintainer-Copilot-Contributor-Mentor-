from pydantic import BaseModel


class FileNode(BaseModel):
    path: str
    imports: list[str] = []
    classes: list[str] = []
    functions: list[str] = []