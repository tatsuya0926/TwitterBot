#coding: UTF-8

import tweepy
import datetime
import twitter_util

TWEET_FILE_NAME = "week_tweets.txt"
SPLITTER = "[--split--]"

def post(text):
    auth = tweepy.OAuthHandler(twitter_util.CONSUMER_KEY, twitter_util.CONSUMER_SECRET)
    auth.set_access_token(twitter_util.ACCESS_TOKEN, twitter_util.ACCESS_SECRET)
    api = tweepy.API(auth)

    api.update_status(status=text)

def main():
    with open(TWEET_FILE_NAME, "r", encoding="utf_8") as f: # tweet内容が含まれたtextファイル読み込み
        file_content = f.read()
        #print(file_content)

        contents = file_content.split(SPLITTER) # SPLITTERでファイルの中身を区切って配列にする
        #print(contents)

        week_num = datetime.date.today().weekday() # 曜日番号を取得（0は月曜日）
        #print(week_num)

        tweet_text = contents[week_num].strip() # tweetファイルの中身から曜日番号に対応する内容を取得
        #print(tweet_text)

        post(tweet_text) # 投稿
        # t = twitter_util.TwitterUtil()
        # t.post(tweet_text) # 投稿

if __name__ == '__main__':
    main()