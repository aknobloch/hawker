from sources.reddit import SubredditSource, TimeFilter

if __name__ != "__main__":

    log.error("Hawker main not called directly, exiting...")
    sys.exit()

reddit = SubredditSource("news")
top_reddit_articles = reddit.fetch_top_articles(5, TimeFilter.DAY)
for article in top_reddit_articles : print(article)