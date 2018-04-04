# crypto google trends slack bot

## setup
- `pip install -r requirements.txt`
- `WEBHOOK_URL = 'TODO'` (L7) を次のファイルに書いてあるもので置き換えて下さい
    https://docs.google.com/document/d/1U1Fn35JGhCymGh3ZyJ_hufJZboMn1uNzpQrilbEazxg/edit?usp=sharing
- configure crontab


## Notes
- ec2の一番小さいやつ(t2.micro)とかでも全然大丈夫です
- 個人的にfree tierのinstanceを立ち上げたのですが、これぐらいでしたらserverlessのAmazon Lambda でもやれると思います
- ec2の場合はcrontabを設定することによって好きな時間にslackにレポートを送れます。このレポジトリにあるcrontabは日本時間の９,12,15,18,21時に送られる設定になっています

 
