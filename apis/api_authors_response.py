from typing import List
from pydantic import BaseModel


class ApiAuthorsResponse(BaseModel):
    """
    Represents list of string returned by the '/author' endpoint.
    Fields:
        authors (List[str]): A list of all authors' names.
    """
    authors: List[str]
