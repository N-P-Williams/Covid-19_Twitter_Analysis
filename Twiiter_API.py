import tweepy
import GetOldTweets3 as got
import pandas as pd
import matplotlib.pyplot as plt

# Login to twitter
# auth = tweepy.OAuthHandler(api_key, api_secret_key)
# auth.set_access_token(access_token, access_secret)
# api = tweepy.API(auth)


def get_tweets(search_word, start_date, end_date, max_tweets):
    """
    :param search_word: String word to be searched
    :param start_date: String date to begin search YYYY-MM-DD
    :param end_date: String date to end search YYYY-MM-DD
    :param max_tweets: Int maximum number of tweets to return
     NW: anything over 10,000 tweets took to long to return for me, also I tend to keep the date range close to a week
    to not miss out on any tweets.
    """
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(search_word) \
        .setSince(start_date) \
        .setUntil(end_date) \
        .setNear('Utah') \
        .setWithin('500mi') \
        .setMaxTweets(max_tweets)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    # put all tweet info in a list of lists

    text_tweets = [[tw.username,
                    tw.text,
                    tw.date,
                    tw.retweets,
                    tw.favorites,
                    tw.mentions,
                    tw.hashtags] for tw in tweets]
    # add all info into a pandas dataframe
    news_df = pd.DataFrame(text_tweets,
                           columns=['User', 'Text', 'Date', 'Favorites', 'Retweets', 'Mentions', 'HashTags'])
    return news_df


if __name__ == "__main__":
    tweet_df = get_tweets(search_word='corona', start_date='2020-01-01', end_date='2020-01-08', max_tweets=100)
    # exporting as an html file
    tweet_df.to_html('twitter_summary.html')

