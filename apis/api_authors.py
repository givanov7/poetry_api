from typing import List
import requests
from apis.api_authors_response import ApiAuthorsResponse
from config.config import config
from config.logger import logger
from validators.validators import validate_authors


class ApiGetAuthors:
    def get_authors(self) -> List[str]:
        """
        Fetches a list of all authors from the API.
        Returns:
            List[str]: A validated list of authors' names.
        """
        endpoint = f"{config.BASE_URL}/author"

        try:
            response = requests.get(endpoint, timeout=10)
            response.raise_for_status()

            authors_list = response.json().get("authors")

            # Validate the structure of the authors list
            validated_authors = validate_authors(authors_list)

            return ApiAuthorsResponse(authors=validated_authors).authors

        except requests.RequestException as e:
            logger.error("HTTP request to %s failed: %s", endpoint, e)
        except ValueError as e:
            logger.error("Invalid JSON or data format: %s", e)
        except Exception as e:
            logger.error("Unexpected error: %s", e)
        return []
