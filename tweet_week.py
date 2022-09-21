#coding: UTF-8

import tweepy
import datetime
import logging
import twitter_util

TWEET_FILE_NAME = "week_tweets.txt"
SPLITTER = "[--split--]"

logging.basicConfig(filename='exec-error.log', level=logging.ERROR, encoding='utf-8')

def post(text):
    """
    Twitterに投稿
    """
    auth = tweepy.OAuthHandler(twitter_util.CONSUMER_KEY, twitter_util.CONSUMER_SECRET)
    auth.set_access_token(twitter_util.ACCESS_TOKEN, twitter_util.ACCESS_SECRET)
    api = tweepy.API(auth)

    api.update_status(status=text)

def main():
    try:
        with open(TWEET_FILE_NAME, "r", encoding="utf_8") as f:
            file_content = f.read()
            contents = file_content.split(SPLITTER) # SPLITTERでファイルの中身を区切って配列にする
            week_num = datetime.date.today().weekday() # 曜日番号を取得（0は月曜日）
            tweet_text = contents[week_num].strip() # tweetファイルの中身から曜日番号に対応する内容を取得
            post(tweet_text)
    except Exception as e:
        logging.error(e)
        logging.error("予期せぬエラーが発生しました")

if __name__ == '__main__':
    main()