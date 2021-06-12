import tweepy

def main():
    CONSUMER_KEY="YCRZpL4h1JZsZ7sEYeJ9Qu75D"
    CONSUMER_SECRET="9OjCGZOdUohZeaVtkxkcohtTNfBLIJ6ZqQVlZt4I6Yk8aJqT71"
    ACCESS_TOKEN="847082587562557440-QuQ3nocTbSZ1JYUxoWDIi9XCVv2gXP6"
    ACCESS_SECERET="l9K6HHQedSniKG7mCxiOUyzvQSXO57szgHW3j7aF7ZwKV"

    auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECERET)
    api=tweepy.API(auth)


    q_list=["#Python","#駆け出しエンジニアと繋がりたい","#プログラミング","#今日の積み上げ"]
    count=10
    for q in q_list:
        print("Now:QUERY-->>{}".format(q))
        search_results=api.search(q=q,count=count) #ツイートのデータであるstatusオブジェクトを取得
        for status in search_results:
            tweet_id=status.id #ツイートidにアクセス
            try:
                api.create_favorite(tweet_id) #ファボ
            except:
                pass

if __name__ == '__main__':
    main()