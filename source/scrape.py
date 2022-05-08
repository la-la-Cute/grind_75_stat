from functools import cache

import requests


class Scraper:
    def __init__(self, url: str) -> None:
        self.url = url

    @cache
    def get(self) -> requests.Response:
        return requests.get(self.url)

    @property
    def text(self) -> str:
        return self.get().text
