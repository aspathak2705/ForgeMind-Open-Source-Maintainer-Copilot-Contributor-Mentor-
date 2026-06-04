from pydantic import BaseModel


class SearchResult(BaseModel):
    file_path: str
    match_type: str
    matched_value: str
    score: int