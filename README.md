# Twitter_project

自動tweet:tweet_week.py

自動いいね:twitter_autoFavorite.py

# セットアップ


### Step 1. install
```
git clone "URL"
```
### Step 2. Twitterからキーの取得

- CONSUMER_KEY = "xxxx"
- CONSUMER_SECRET = "xxxx"
- ACCESS_TOKEN = "xxxx"
- ACCESS_SECERET = "xxxx"

### Step 3. 自動化

1.crontab -eで、crontabを開き、iキーを入力
```
crontab -e
```
2.PATHと実行させたい日時と実行したいファイルを記述
```
PATH=XXXX
0 7 * * * python /Users/****-pc/Twitter_project/tweet_week.py > /Users/****-pc/Twitter_project/exec-error.log 2>&1

0 */1 * * * python /Users/****-pc/Twitter_project/twitter_autoFavorite.py > /Users/****-pc/Twitter_project/exec-error.log 2>&1
```
3.PATHと実行内容（上記参照）を入力した後、escキーを入力。:wqを押し、そしてreturnで上書き保存

・現在実行されているcronのリスト確認
```
crontab -l
```
・cron内の情報すべて削除(注：crontab -e との押し間違い注意)
```
crontab -r
```
・実行されているものの前に#を入力することで実行させなくできる

・保存せずにvimを抜ける
```
:q!
```
### おまけ（実行順番）

export EDITOR=vim

echo $PATH

crontab -e

i

PATH=***

#(分) (時) (日) (月) (曜日)  (実行するコマンド)

* * * * * (実行するコマンド) > /Users/****-pc/Desktop/exec-error.log 2>&1 (エラーがあった際、それを表示)

esc

:wq

return
