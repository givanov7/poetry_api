from typing import List
from pydantic import BaseModel


class ApiPoemByTitleResponse(BaseModel):
    """
    Represents the structure of a poem returned by the '/title/{title}' endpoint.
    Fields:
        title (str): The title of the poem.
        author (str): The author's name.
        lines (List[str]): The poem's content, split into lines.
        linecount (str): The number of lines in the poem, as a string.
    """
    title: str
    author: str
    lines: List[str]
    linecount: str
