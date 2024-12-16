### 第11週 電子メールの操作 (ver.0.1) ###

## [w11] 準備 ##

# w11.1 リポジトリの最新化
~$ cd pp2
~/pp2$ git pull

# w11.2 演習用ファイルの表示
~/pp2$ tree w11

# w11.3 README.mdの表示
~/pp2$ emacs -nw w11/README.md

# w11.4 クライアントシークレットの取得
# w11.4.1 プロジェクトの作成
＊w10.4.1 プロジェクトの作成 を実行

# w11.4.2. ライブラリの有効化
＊w10.4.2 ライブラリの有効化 に加えて以下を実行

# w11.4.2.1 Gmail APIの有効化
https://console.cloud.google.com
-> Navigation menu（画面左上のハンバーガーアイコン）
-> APIs & Services -> Library
-> search "Gmail" -> Gmail API -> ENABLE

# w11.4.3. OAuthの設定
＊w10.4.3. OAuthの設定 を実行

# w11.4.4. クライアントシークレットの入手
＊w10.4.4. クライアントシークレットの入手 を実行

# w11.4.5 クライアントシークレットの配置
~/pp2/w11$ ls
~/pp2/w11$ ./command.sh; ls; ls output
Filesで ~/pp2/w11/output を開く（client_secret...jsonを確認）

## [w11.kp1] ezgmailモジュール ##

# w11.kp1.1 プログラムの実行（メールの送信）
~/pp2/w11$ cd kp1
~/pp2/w11/kp1$ ls
~/pp2/w11/kp1$ ./command.sh
-> Chromeブラウザが起動する
-> Googleアカウントを選択 -> Advanced -> Go to myapp (usafe) -> Continue
-> Filesで ~/pp2/w11/output/token.jsonを確認

-> Chromeブラウザ -> Gmail -> テストメールの送信を確認

~/pp2/w11/kp1$ ./command.sh
-> Chromeブラウザ -> Gmail -> テストメールの再送信を確認

# w11.kp1.2 プログラムの確認
C-x C-f ~/pp2/w11/kp1/gmail.py

## [w11.kp2] Gmailの操作 ##

# w11.kp2.1 プログラムの実行（受信メールの検索）
~/pp2/w11/kp1$ cd ../kp2
~/pp2/w11/kp2$ ls
~/pp2/w11/kp2$ ./command.sh
-> 件名にpp2_w11_kp1という文字列が含まれるメールを受信箱から検索する

# w11.kp2.2 プログラムの確認
C-x C-f ~/pp2/w11/kp2/gmail_db.py

## [w11.kp3] 会費のリマインダーメールを送信するプログラム ##

# w11.kp3.1 プログラムの実行（リマインダーメールの送信）
~/pp2/w11/kp2$ cd ../kp3
~/pp2/w11/kp3$ ls
~/pp2/w11/kp3$ ./command.sh
-> Chromeブラウザが起動する
-> Googleアカウントを選択 -> Advanced -> Go to myapp (usafe) -> Continue
-> Filesで ~/pp2/w11/output/token-sheets.pickleを確認

~/pp2/w11/kp3$ ./command.sh
-> Chromeブラウザが起動する
-> Googleアカウントを選択 -> Advanced -> Go to myapp (usafe) -> Continue
-> Filesで ~/pp2/w11/output/token-drive.pickleを確認

-> Chromeブラウザ -> Google Drive -> My Drive -> pp2_w11_kp3をダブルクリック
-> Google Sheetsでpp2_w11_kp3（以後，会計帳簿と呼ぶ）の内容を確認

＊Chromeブラウザで雛形
https://docs.google.com/spreadsheets/d/1tHcpMC_Tj9MSkCpXAvIl4tldjxo8wPJZv7uBSigRjF4
を開き，会計帳簿の1番目の会員に自分が登録されていることを確認

-> Chromeブラウザ -> Gmail -> リマインダーメールの送信を確認

~/pp2/w11/kp3$ ./command.sh
-> Chromeブラウザ -> Gmail -> リマインダーメールの再送信を確認

# w11.kp3.2 プログラムの実行（会計帳簿の自動更新）
-> Chromeブラウザ -> Gmail -> リマインダーメールへの返信で入金を連絡

~/pp2/w11/kp3$ ./command.sh
-> Chromeブラウザ -> Gmail 
-> 入金の会計帳簿への記録とリマインダーメールの送信停止を確認

# w11.kp3.3 プログラムの確認
C-x C-f ~/pp2/w11/kp3/accountant.py

＊google_sheets.pyはw10で説明済み
