import os


class Config:
    def __init__(self):
        """
        Base URL and Current Dir configuration
        """

        self.BASE_URL = 'https://poetrydb.org'
        self.CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

config = Config()
