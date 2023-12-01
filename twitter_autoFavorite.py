import tweepy
import logging
import twitter_util

logging.basicConfig(filename='exec-error.log',
                    level=logging.ERROR, encoding='utf-8')


def main():
    try:
        logging.info("start.")
        auth = tweepy.OAuthHandler(
            twitter_util.CONSUMER_KEY, twitter_util.CONSUMER_SECRET)
        auth.set_access_token(twitter_util.ACCESS_TOKEN,
                              twitter_util.ACCESS_SECRET)
        api = tweepy.API(auth)

        count = 20
        q_list = ["#データサイエンティスト", "#機械学習", "#machine learning"]
        for q in q_list:
            logging.info(f"Now:QUERY-->>{q}")
            # ツイートのデータであるstatusオブジェクトを取得
            search_results = api.search(q=q, count=count)
            for status in search_results:
                try:
                    api.create_favorite(status.id)  # ファボ
                except Exception as e:
                    logging.error("ファボに失敗しました。")
    except Exception as e:
        logging.error("予期せぬエラーが発生しました")
        logging.error(e)
    finally:
        logging.info("finished.")


if __name__ == '__main__':
    main()
