import datetime
import tweepy
import logging
import re

from django.shortcuts import render
from tweepy.error import TweepError

from .enums import Twitter


logger = logging.getLogger(__name__)


def index(request):
    auth = tweepy.OAuthHandler(Twitter.CONSUMER_TOKEN.value,
                               Twitter.CONSUMER_SECRET.value)
    auth.set_access_token(Twitter.APP_TOKEN.value,
                          Twitter.APP_SECRET.value)
    api = tweepy.API(auth, wait_on_rate_limit=Twitter.WAIT_ON_RATE_LIMIT.value)
    datas = dict()
    try:
        public_tweets = api.home_timeline(count=Twitter.TWEETS_LIMIT.value)
        list_tweets = list()
        for tweet in public_tweets:
            tweet_text = tweet.text
            tweet_text = re.sub(r"(@\w*)",
                                r"<a href='https://twitter.com/%s' target='_blank' class='poke_tweet'>\1</a>"
                                % tweet.author.screen_name, tweet_text)
            created_at = datetime.datetime(tweet.created_at.year, tweet.created_at.month, tweet.created_at.day,
                                           tweet.created_at.hour, tweet.created_at.minute, tweet.created_at.second)
            list_tweets.append({"author": tweet.author.name, "text": tweet_text,
                                "created_at": created_at.strftime("%Y-%m-%d %H:%M:%S")})
        datas.update({"tweets": list_tweets})
    except TweepError:
        logger.error(Twitter.COULD_NOT_AUTHENTICATE.value)
    return render(request, "index.html", datas)
