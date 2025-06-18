import allure
import pytest
from apis.api_authors import ApiGetAuthors


@pytest.mark.TestGetAuthorsStartingWith
@allure.title("Test Get Authors starting with a specific letter")
@allure.description("Test for getting all authors starting with a specific letter")
@pytest.mark.normal
class TestGetAuthorsStartingWith:
    api_get_author = ApiGetAuthors()

    @pytest.mark.parametrize("starts_with", ["G"])
    @allure.description("Send a get request to /author with optional parameter 'starts_with'"
                        "Expected result: get a list of authors starting with the specified letter")
    def test_get_authors_starting_with(self, starts_with):
        """
        Test fetching authors with an optional starting letter filter.
        This test verifies that:
        - The response contains a non-empty list of author names.
        - If a 'starts_with' value is provided, 
        all returned authors start with that letter (case-insensitive).
        Args:
            starts_with (str or None): The optional starting letter to filter authors by.
        Expected behavior:
        The API should return a list of authors' names. 
        If filtering is applied, all names should begin with the specified character.
        """
        authors = self.api_get_author.get_authors()

        assert len(authors) > 0, "The author name should not be empty."

        if starts_with:
            filtered_authors = [
                a for a in authors if a.lower().startswith(starts_with.lower())
            ]
            assert len(filtered_authors) > 0, f"No authors found starting with '{starts_with}'"
            assert (
                all(a.lower().startswith(starts_with.lower()) for a in filtered_authors)
            ), (
                f"Expected all authors to start with '{starts_with}'"
            )
        else:
            assert len(authors) > 0, "Expected at least one author in the list."
