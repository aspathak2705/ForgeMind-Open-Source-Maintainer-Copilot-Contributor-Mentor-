from pydantic import BaseModel

class FunctionNode(BaseModel):
    name: str
    args: list[str]
    docstring: str
    file_path: str = ""