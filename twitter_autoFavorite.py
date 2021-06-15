import tweepy
import twitter_util

def main():
    api=tweepy.API(twitter_util.auth) #キーの取得

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