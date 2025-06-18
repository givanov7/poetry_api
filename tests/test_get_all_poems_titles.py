import allure
import pytest
from apis.api_all_poems_titles import ApiGetAllPoemsTitles


@pytest.mark.TestGetAllPoemsTitles
@allure.title("Test Get All Poems Titles")
@allure.description("Test for getting all poems titles")
@pytest.mark.normal
class TestGetAllPoemsTitles:
    """
    Get all poems' titles.
    """
    api_get_all_poems_titles = ApiGetAllPoemsTitles()

    @allure.description("Send a get request to /title without any parameters"
                        "Expected result: get a list with all poems titles")
    def test_get_all_poems_titles(self):
        """
        Test fetching all poem titles from the API.
        This test verifies that:
        - The response returns a non-empty list of poem titles.
        - Each item in the returned list is a string.
        Expected behavior:
        The API should return at least one poem title, and all entries should be strings.
        """
        poems = self.api_get_all_poems_titles.get_poems()

        assert len(poems) > 0, "The poems titles list should not be empty."

        assert (
            all(isinstance(poem, str) for poem in poems)
        ), (
            "All items in the poems list should be strings."
        )
