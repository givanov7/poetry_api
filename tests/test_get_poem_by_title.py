import pytest
import allure
from apis.api_poem_by_title import ApiGetPoemByTitle


@pytest.mark.TestGetPoemByTitle
@allure.title("Test Get Poem By Title")
@allure.description("Test for getting a poem by title")
@pytest.mark.normal
class TestGetPoemByTitle:
    api_get_poem_by_title = ApiGetPoemByTitle()

    @allure.description("Send a get request to /title with parameter 'title'"
                        "Expected result: get a poem by title")
    def test_get_poem_by_title(self):
        """
        Test fetching a poem by its title and validating its content.

        This test verifies that:
        - The API returns at least one poem for the given title.
        - The poem's title matches the expected title (ignoring leading/trailing whitespace).
        - The poem's author matches the expected author.
        - The poem's line count matches the expected value.

        Expected behavior:
        When querying the poem titled "Thoughts On The Works Of Providence",
        the API should return a poem authored by "Phillis Wheatley" with exactly 131 lines.
        """
        title = "Thoughts On The Works Of Providence"
        author = "Phillis Wheatley"
        linecount = 131
        poems = self.api_get_poem_by_title.get_poem_by_title(title)

        assert len(poems) > 0, "Expected at least one poem"
        for p in poems:
            assert (
                p.title.strip() == title.strip()
            ), (
                f"Expected title to be '{title}', but got '{p.title}'."
            )

            assert (
                p.author.strip() == author.strip()
            ), (
                f"Expected author to be '{author}', but got '{p.author}'."
            )

            assert (
                int(p.linecount) == linecount
            ), (f"Expected linecount to be '{linecount}', but got '{p.linecount}'."
            )
