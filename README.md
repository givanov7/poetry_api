# POETRY_API Test Suite

## 🚀 Project Overview

A Python project for testing poetry-related API endpoints for https://poetrydb.org/index.html using `requests`, `pytest`, and `pydantic`, and `Allure` for reporting. The suite validates data returned by the API, including all poems titles, authors names starting with specific letter, and found poem by title.

## ⚙️ Installation

1. **Clone the repo**  

2. **Create & activate a virtual environment**  

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate

3. **Install all packages and dependencies outlined in the requirements.txt file**  

   ```bash
   pip3 install -r requirements.txt

4. **Run the tests and generate & serve Allure report:**

   ```bash
   pytest --alluredir=reports/allure-results


- Open the generated allure reports:

   ```bash
   allure serve reports/allure-results

5. **Project Structure**

```plaintext
├── apis/
│ ├── api_all_poems_titles_response.py
│ ├── api_all_poems_titles.py
│ ├── api_authors_response.py
│ ├── api_authors.py
│ ├── api_poem_by_title_response.py
│ └── api_poem_by_title.py
├── config/
│ ├── config.py
│ └── logger.py
├── tests/
│ ├── test_get_all_poems_titles.py
│ ├── test_get_authors_starting_with.py
│ └── test_get_poem_by_title.py
├── reports/
├── validators/
│  └── validators.py
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

6. **Test Cases**

| Test Case ID | Test file                         | Description                                                    | Endpoint           | Expected result                                                                                                                                                                                                                         |
|--------------|-----------------------------------|----------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC-01        | test_get_all_poems_titles.py      | Test getting all poems titles from the endpoint                | GET /title         | - a non-empty list of poems' titles is returned - each item in the returned list is a string                                                                                                                                            |
| TC-02        | test_get_authors_starting_with.py | Test getting all or filtered by the first letter authors' list | GET /author        | - a non-empty list of authors is returned - if filtering is applied, all authors' names should begin with the specified character                                                                                                       |
| TC-03        | test_get_poem_by_title.py         | Test getting poem by its title                                 | GET /title/{title} | - a non-empty list of poem's objects is returned - the poem's title matches the expected title (ignoring leading/trailing whitespace) - The poem's author matches the expected author - The poem's linecount matches the expected value |

7. **Video**

https://github.com/user-attachments/assets/d5831264-de1b-499b-9d48-1ed75e3c924b


