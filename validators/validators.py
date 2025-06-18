from typing import List, Dict


def validate_authors(authors: List[str]) -> List[str]:
    """
    Validates that the authors list is not empty and contains only strings.

    :param authors: A list of author names.
    :return: The validated list of authors.
    """
    if not isinstance(authors, list) or not all(isinstance(a, str) and a.strip() for a in authors):
        raise ValueError("Authors list must contain at least one non-empty string")
    return authors


def validate_poems(titles: List[str]) -> List[str]:
    """
    Validates that the poems list is not empty and contains only strings.

    :param poems: A list of poems title.
    :return: The validated list of poems.
    """
    if not titles or not all(isinstance(title, str) for title in titles):
        raise ValueError("Poems list must contain at least one non-empty string")
    return titles


def validate_poem(poems: List[Dict]) -> List[Dict]:
    """
    Validates a list of poem dictionaries.

    Args:
        poems (List[Dict]): A list of poem objects from the API.

    Returns:
        List[Dict]: The validated list of poems.

    Raises:
        ValueError: If the input is not valid or contains invalid items.
    """
    if not isinstance(poems, list):
        raise ValueError("Poems must be provided as a list.")

    if not poems:
        raise ValueError("Poem list is empty.")

    valid_poems = []
    for i, poem in enumerate(poems):
        if not isinstance(poem, dict):
            raise ValueError(f"Item at index {i} is not a dictionary.")
        
        for field in ["title", "author", "lines", "linecount"]:
            if field not in poem:
                raise ValueError(f"Poem at index {i} is missing required field '{field}'.")

        if not isinstance(poem["lines"], list) or not poem["lines"]:
            raise ValueError(f"Poem at index {i} has invalid or empty 'lines' field.")

        valid_poems.append(poem)

    return valid_poems
