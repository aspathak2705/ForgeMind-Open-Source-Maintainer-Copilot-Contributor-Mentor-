from pydantic import BaseModel

class ClassNode(BaseModel):
    name: str
    methods: list[str] = []
    base_classes: list[str] = []
    file_path: str
    