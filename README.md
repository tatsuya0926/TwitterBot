# Twitter_project

自動tweet:tweet_week.py

自動いいね:twitter_autoFavorite.py

# セットアップ


### Step 1. レポジトリをclone
```
git clone "URL"
```
### Step 2. Twitterからキーの取得

Twitter Developerから取得してください。

- CONSUMER_KEY = "xxxx"
- CONSUMER_SECRET = "xxxx"
- ACCESS_TOKEN = "xxxx"
- ACCESS_SECERET = "xxxx"

### Step 3. 自動化

今回はMac user向けにcron(Mac_os)で自動化します。（Windowsならタイムスケジューラーで）

1.crontab -eで、crontabを開き、iキーを入力

入力可能になるので以下を入力。
```
crontab -e
```
2.PATHと実行させたい日時と実行したいファイルを記述
```
PATH=XXXX
0 7 * * * python /Users/****/TwitterBot/tweet_week.py > /Users/****/TwitterBot/exec-error.log 2>&1

0 */1 * * * python /Users/****/TwitterBot/twitter_autoFavorite.py > /Users/****/TwitterBot/exec-error.log 2>&1
```
PATHは
```
echo $PATH
```
で取得できます

3.PATHと実行内容（上記参照）を入力した後、escキーを入力。:wqを押し、そしてreturnで上書き保存
```
:wq
```

# 付録

##croncode

・現在実行されているcronのリスト確認
```
crontab -l
```
・cron内の情報すべて削除(注：crontab -e との押し間違い注意)
```
crontab -r
```
・保存せずにvimを抜ける
```
:q!
```
・一番前に#でコメントアウト

##仮想環境pyenvを用いてサードパーティーのライブラリをインストールして使用

## 実行順序

export EDITOR=vim

echo $PATH

crontab -e

i

PATH=***

#(分) (時) (日) (月) (曜日)  (実行するコマンド)

* * * * * (実行するソースコード) > /Users/****/TwitterBot/exec-error.log 2>&1 (エラーがあった際、それを表示)

esc

:wq

return
