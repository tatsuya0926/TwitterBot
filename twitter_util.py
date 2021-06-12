#coding: UTF-8

import twitter

class TwitterUtil:
    auth = twitter.OAuth(consumer_key="YCRZpL4h1JZsZ7sEYeJ9Qu75D",
                         consumer_secret="9OjCGZOdUohZeaVtkxkcohtTNfBLIJ6ZqQVlZt4I6Yk8aJqT71",
                         token="847082587562557440-QuQ3nocTbSZ1JYUxoWDIi9XCVv2gXP6",
                         token_secret="l9K6HHQedSniKG7mCxiOUyzvQSXO57szgHW3j7aF7ZwKV")

    def post(self, text):
        tw = twitter.Twitter(auth=self.auth)
        tw.statuses.update(status=text) 