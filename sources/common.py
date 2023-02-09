import abc
from enum import Enum
from newspaper import Article


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


class WebArticle:
    def __init__(self, url: str):
        self._url = url
        self._article = Article(self._url)

        # Lazily initialized via getter methods
        self._title = None
        self._content = None
        self._summary = None
        self._keywords = None

    def __str__(self):
        return """
        Title: {}
        URL: {}
        Keywords: {}
        Content Sample: {} ...
        """.format(
            self.get_title(), self._url, self.get_keywords(), self.get_summary()
        )

    def get_url(self):
        return self._url

    def get_title(self):
        if self._title is None:
            self._title = "TODO: Generate title from article"

        return self._title

    def get_full_content(self):
        if self._content is None:
            self._article.download()
            self._article.parse()
            self._content = self._article.text.replace("\n", " ").strip()

        return self._content

    def get_summary(self):
        if self._summary is None:
            # TODO: better summary generation
            self._summary = self.get_full_content()[0:100].strip().replace("\n", "")
        
        return self._summary

    def get_keywords(self):
        if self._keywords is None:
            self._keywords = ["TODO: Generate keywords from article"]

        return self._keywords
