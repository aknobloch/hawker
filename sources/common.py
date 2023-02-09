import abc
from enum import Enum


class TimeFilter(Enum):
    HOUR = "hour"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"


class NewsSourceInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, "fetch_top_articles") and callable(
            subclass.fetch_top_articles
        )

    @abc.abstractmethod
    def fetch_top_articles(self, num: int, time_filter: TimeFilter):
        """Fetch |num| articles from this source"""
        raise NotImplementedError


class Article:
    def __init__(self, url: str, title: str, content: str):
        self._url = url
        self._title = title
        self._content = content

    def __str__(self):
        return """
        Title: {}
        URL: {}
        Content Sample: {} ...
        """.format(
            self._title, self._url, self._content[0:100].strip().replace("\n", "")
        )

    def get_url(self):
        return self._url

    def get_title(self):
        return self._title

    def get_content(self):
        return self._content
