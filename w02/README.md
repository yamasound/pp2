### 第2週 パターンマッチ (ver.0.1) ###

## [w02] 準備 ##

# w02.1 リポジトリの最新化
~$ cd pp2
~/pp2$ git pull

# w02.2 演習用ファイルの表示
~/pp2$ tree w02

# w01.3 README.mdの表示
~/pp2$ emacs -nw w02/README.md

# w01.4 パッケージのインストール
C-x 2 でバッファを分割
C-x o で次のバッファへ移動
C-x a でバッファ内でTerminalを起動

~/pp2/w02$ ./command.sh

## [w02.kp1] reモジュールとRegexオブジェクトによる正規表現の処理 ##

# w02.kp1.1 プログラムの実行
~/pp2/w02$ cd kp1
~/pp2/w02/kp1$ ls
~/pp2/w02/kp1$ ./command.sh

# w02.kp1.2 プログラムの確認（README.mdを見ながら）
C-x C-f ~/pp2/w02/kp1/detect_date.py
C-x k RET

# w02.kp1.3 プログラムの確認（実行結果を見ながら）
C-x o で上のバッファへ移動
C-x C-f ~/pp2/w02/kp1/detect_date.py
C-x k RET

## [w02.kp2] search, findall, sub メソッド ##

# w02.kp2.a1 プログラムの実行
C-x o で下のバッファへ移動
~/pp2/w02/kp1$ cd ../kp2_search
~/pp2/w02/kp2_search$ ls
~/pp2/w02/kp2_search$ ./command.sh

[Emacsのターミナルのショートカット]
C-c C-j lineモードへの移行
C-c C-k charモードへの移行

# w02.kp2.a2 プログラムの確認
C-x o で上のバッファへ移動
C-x C-f ~/pp2/w02/kp2_search/check_password.py
C-x k RET

# w02.kp2.b1 入力データの確認
C-x o で下のバッファへ移動
~/pp2/w02/kp2_search$ cd ../kp2_findall
~/pp2/w02/kp2_findall$ ls
~/pp2/w02/kp2_findall$ less input/juroku.txt

[lessのキー操作]
C-n で下へ移動
C-p で上へ移動
q で終了

# w02.kp2.b2 プログラムの実行
~/pp2/w02/kp2_findall$ ./command.sh

# w02.kp2.b3 プログラムの確認
C-x o で上のバッファへ移動
C-x C-f ~/pp2/w02/kp2_findall/check_phones.py 
C-x k RET

# w02.kp2.c1 プログラムの実行
C-x o で下のバッファへ移動
~/pp2/w02/kp2_findall$ cd ../kp2_sub
~/pp2/w02/kp2_sub$ ls
~/pp2/w02/kp2_sub$ ./command.sh

# w02.kp2.c2 プログラムの確認
C-x o で上のバッファへ移動
C-x C-f ~/pp2/w02/kp2_sub/restrip.py
C-x k RET

## [w02.kp3] 電話番号と電子メールアドレスの抽出プログラム ##

# w02.kp3.1 プログラムの実行
C-x o で下のバッファへ移動
~/pp2/w02/kp2_sub$ cd ../kp3
~/pp2/w02/kp3$ ls
~/pp2/w02/kp3$ ./command.sh

# w02.kp3.2 プログラムの確認
C-x o で上のバッファへ移動
C-x C-f ~/pp2/w02/kp3/extract_phones_or_emails_on_the_clipboard.py
C-x k RET

# w02.kp3.3 電話番号の抽出
Chromeで「十六銀行 問い合わせ」にアクセスする
https://www.juroku.co.jp/aboutus/contact.html

「十六銀行 問い合わせ」のページから以下をコピー
-----
ご利用停止の受付
キャッシュカード・通帳・証書・届出印の紛失、盗難時
インターネットバンキングの不正使用時
電話番号	受付時間
0120-69-5416	24時間365日
海外からのご利用等、上記番号がご利用いただけない場合は、058-266-2678へおかけください（通話料有料）。

JCBデビットのカード紛失・盗難時

電話番号	受付時間
0120-794-082	24時間365日
　※海外からの連絡先は、JCBのホームページをご覧ください。
-----

プログラムの実行
C-x o で下のバッファへ移動
~/pp2/w02/kp3$ ./command.sh 

# w02.kp3.4 電話番号とメールアドレスの抽出
Chromeで「秋田県立大学」にアクセスする
https://www.akita-pu.ac.jp/

「秋田県立大学」のページから以下をコピー
-----
電話：018-872-1500／FAX：018-872-1670／MAIL：koho_akita@akita-pu.ac.jp
(法人番号　8410005001507)
-----

プログラムの実行
~/pp2/w02/kp3$ ./command.sh 
