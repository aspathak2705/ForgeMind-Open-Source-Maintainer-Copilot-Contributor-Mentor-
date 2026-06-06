from pydantic import BaseModel

from core.models.class_node import (
    ClassNode,
)


class FileNode(BaseModel):

    path: str

    imports: list[str] = []

    classes: list[ClassNode] = []

    functions: list[str] = []