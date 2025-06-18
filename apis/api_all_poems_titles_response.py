from typing import List
from pydantic import BaseModel


class ApiAllPoemsTitlesResponse(BaseModel):
    """
    Represents list of strings returned by the '/title' endpoint.
    Fields:
        titles (List[str]): A list of all poems titles.
    """
    titles: List[str]
