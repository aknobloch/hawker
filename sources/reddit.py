import praw
import credentials.reddit
from sources.common import NewsSourceInterface, Article, TimeFilter
from newspaper import Article as NewspaperArticle

class SubredditSource(NewsSourceInterface):

    MIN_CONTENT_CHAR_LENGTH = 500

    def __init__(self, subreddit_name: str):
        self._subreddit = subreddit_name
        self._reddit = praw.Reddit(
            username=credentials.reddit.Username(),
            password=credentials.reddit.Password(),
            client_id=credentials.reddit.ClientId(),
            client_secret=credentials.reddit.ClientSecret(),
            user_agent="hawker by /u/aarondevelops",
        )

    def fetch_top_articles(self, num: int, time_filter: TimeFilter):
        top_articles = []

        for submission in self._reddit.subreddit(self._subreddit).top(
            limit=num, time_filter=time_filter.value
        ):
            news_article = NewspaperArticle(submission.url)
            news_article.download()
            news_article.parse()
            
            if(len(news_article.text) > self.MIN_CONTENT_CHAR_LENGTH):
                article = Article(submission.url, submission.title, news_article.text)
                top_articles.append(article)

        return top_articles
