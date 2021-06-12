#coding: UTF-8

import twitter_util

TWEET_FILE_NAME = "/Users/miyata-pc/Desktop/MyPython/tweet/text_tweet.txt"

def main():
  with open(TWEET_FILE_NAME, "r", encoding="utf_8") as f:
    file_content = f.read()

    t = twitter_util.TwitterUtil()
    t.post(file_content)

if __name__ == '__main__':
    main()