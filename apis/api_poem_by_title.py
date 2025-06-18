from typing import List
import requests
from apis.api_poem_by_title_response import ApiPoemByTitleResponse
from config.config import config
from config.logger import logger
from validators.validators import validate_poem


class ApiGetPoemByTitle:
    def get_poem_by_title(self, title: str) -> List[ApiPoemByTitleResponse]:
        """
        Retrieve poem by a given title from the API.
        Args:
            title (str): The title of the poem to fetch.
        Returns:
            List[ApiPoemByTitleResponse]: A list of parsed and validated poem's objects.
        """
        # Ensure title is URL-safe
        encoded_title = title.strip()
        endpoint = f"{config.BASE_URL}/title/{encoded_title}"

        try:
            response = requests.get(endpoint, timeout=10)
            response.raise_for_status()

            poem_data = response.json()

            # Validate the structure of the poem data
            validated_poems = validate_poem(poem_data)

            return [ApiPoemByTitleResponse(**poem) for poem in validated_poems]

        except requests.RequestException as e:
            logger.error("HTTP error while fetching poem titled %s: %s", encoded_title, e)
        except ValueError as e:
            logger.error("Invalid JSON in response for title %s: %s", encoded_title, e)
        except Exception as e:
            logger.error("Unexpected error during poem retrieval: %s: %s", encoded_title, e)
        return []
