from typing import List
import requests
from apis.api_all_poems_titles_response import ApiAllPoemsTitlesResponse
from config.config import config
from config.logger import logger
from validators.validators import validate_poems


class ApiGetAllPoemsTitles:
    def get_poems(self) -> List[str]:
        """
        Retrieve all poems from the API.
        Returns:
            List[str]: A list of all poems titles.
        """
        endpoint = f"{config.BASE_URL}/title"

        try:
            response = requests.get(endpoint, timeout=10)
            response.raise_for_status()

            all_poems_titles_list = response.json().get("titles")

            # Validate the structure of the poems list
            validated_poems_titles = validate_poems(all_poems_titles_list)

            return ApiAllPoemsTitlesResponse(titles=validated_poems_titles).titles

        except requests.RequestException as e:
            logger.error("HTTP request to %s failed: %s", endpoint, e)
        except ValueError as e:
            logger.error("Invalid JSON or data format: %s", e)
        except Exception as e:
            logger.error("Unexpected error: %s", e)
        return []
