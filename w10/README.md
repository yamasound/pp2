### 第10週 Google Sheets の操作 (ver.0.1) ###

## [w10] 準備 ##

# w10.1 リポジトリの最新化
~$ cd pp2
~/pp2$ git pull

# w10.2 演習用ファイルの表示
~/pp2$ tree w10

# w10.3 README.mdの表示
~/pp2$ emacs -nw w10/README.md

# w10.4 クライアントシークレットの取得
# w10.4.1 プロジェクトの作成
https://console.cloud.google.com
Project menu（画面上部にあるプロジェクトのプルダウン）
-> NEW PROJECT
  Project name: pp2v1
  Location: No organization
  
＊大学のGoogleアカウントの場合
    Organization: akita-pu.ac.jp
    Location: akita-pu.ac.jp

-> CREATE

-> Project menu（画面上部にあるプロジェクトのプルダウン）
-> pp2v1をクリック

# w10.4.2. ライブラリの有効化
# w10.4.2.1 Google Sheets APIの有効化
-> Navigation menu（画面左上のハンバーガーアイコン）
-> APIs & Services -> Library
-> search "Google Sheets" -> Google Sheets API -> ENABLE

# w10.4.2.2 Google Drive APIの有効化
-> Navigation menu
-> APIs & Services -> Library
-> search "Google Drive" -> Google Drive API -> ENABLE

# w10.4.3. OAuthの設定
-> Navigation menu
-> APIs & Services -> OAuth consent screen

（OAuth consent screenが表示される）
-> External -> CREATE
  App information
    App name: myapp
    User support email: YOUR EMAIL ADDRESS
  Developer contact information
    Email addresses: YOUR EMAIL ADDRESS
-> SAVE AND CONTINUE

（Scopesが表示される）
-> SAVE AND CONTINUE

（Test usersが表示される）
-> SAVE AND CONTINUE

（Summaryが表示される）
-> BACK TO DASHBOARD

（myappが表示される）
-> Publishing statusのPUBLISH APPをクリック -> CONFIRM
（TestingからIn productionへ変わる）

# w10.4.4. クライアントシークレットの入手
-> Navigation menu
-> APIs & Services -> Credentials 
-> （画面上部の）"+ CREATE CREDENTIALS"
-> OAuth client ID
  Application type: Desktop app
  Name: Desktop client 1
-> CREATE -> DOWNLOAD JSON -> OK

# w10.4.5 クライアントシークレットの配置
~/pp2/w10$ ls
~/pp2/w10$ ./command.sh; ls; ls output
Filesで ~/pp2/w10/output を開く（client_secret...jsonを確認）

## [w10.kp1] ezsheetsモジュールとSpreadsheetオブジェクト ##

# w10.kp1.1 プログラムの実行（Google Sheetsのファイルを作る）
~/pp2/w10$ cd kp1
~/pp2/w10/kp1$ ls
~/pp2/w10/kp1$ ./command.sh
-> Chromeブラウザが起動する
-> Googleアカウントを選択 -> Advanced -> Go to myapp (usafe) -> Continue
-> Filesで ~/pp2/w10/output/token-sheets.pickleを確認

~/pp2/w10/kp1$ ./command.sh
-> Chromeブラウザが起動する
-> Googleアカウントを選択 -> Advanced -> Go to myapp (usafe) -> Continue
-> Filesで ~/pp2/w10/output/token-drive.pickleを確認

-> Chromeブラウザ -> Google Drive -> My Drive -> pp2_w10_kp1をダブルクリック
-> 空のGoogle Sheetsのファイルが作成されていることを確認
-> 空のpp2_w10_kp1を削除

Chromeブラウザで
https://docs.google.com/spreadsheets/d/15MY0RZOLMMGsFLslnUh7L0xRTjuA6XCRF5pNdaDeuwg
を開き，内容を確認する

~/pp2/w10/kp1$ ./command.sh 15MY0RZOLMMGsFLslnUh7L0xRTjuA6XCRF5pNdaDeuwg
-> 商品リストのGoogle Sheetsのファイルに変更されていることを確認

# w10.kp1.2 プログラムの確認
C-x C-f ~/pp2/w10/kp1/google_sheets.py

## [w10.kp2] スプレッドシートの操作 ##

# w10.kp2.1 プログラムの実行（スプレッドシートへ書き込む）
~/pp2/w10/kp1$ cd ../kp2
~/pp2/w10/kp2$ ls
~/pp2/w10/kp2$ ./command.sh
-> Chromeブラウザ -> Google Drive -> My Drive -> pp2_w10_kp2をダブルクリック
-> My petsのGoogle Sheetsのファイルが作成されていることを確認

# w10.kp2.2 プログラムの確認
C-x C-f ~/pp2/w10/kp2/my_pets.py

# w10.kp2.3 プログラムの改変と実行
＊ZophieのWeightを10から9へ変更する
~/pp2/w10/kp2$ ./command.sh
-> Google SheetsでZophieのWeightが訂正されたことを確認

## [w10.kp3] スプレッドシートの内容の検算 ##

# w10.kp3.1 プログラムの実行（請求額を検算する）
Chromeブラウザで
https://docs.google.com/spreadsheets/d/17ac2UBtvIQSLJ468s4ag9DoLlrvZA6pcD88jgf_E19U
を開き，誤っている箇所を探す

~/pp2/w10/kp2$ cd ../kp3
~/pp2/w10/kp3$ ls
~/pp2/w10/kp3$ ./command.sh
-> Chromeブラウザ -> Google Drive -> My Drive -> pp2_w10_kp3をダブルクリック
-> Google Sheetsで請求書の内容が訂正されたことを確認

# w10.kp3.2 プログラムの確認
C-x C-f ~/pp2/w10/kp3/wrong_invoices.py
