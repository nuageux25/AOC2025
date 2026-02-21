import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()


class Utils:
    """Connects to the platform and returns the data set for each exercise"""
    def __init__(self, url_of_the_day: str):
        self.url_of_the_day = url_of_the_day
        self.cookies = json.loads((os.getenv("AOC_SESSION")))
        self.puzzle = self.get_puzzle()

    def get_puzzle(self) -> str:
        return requests.get(self.url_of_the_day,cookies=self.cookies).text
