### 第14週 GUIの操作 (ver.0.1) ###

## [w14] 準備 ##

# w14.1 リポジトリの最新化
~$ cd pp2
~/pp2$ git pull

# w14.2 演習用ファイルの表示
~/pp2$ tree w14

# w14.3 README.mdの表示
~/pp2$ emacs -nw w14/README.md

# w14.4 パッケージのインストール
C-x 2 でバッファを分割
C-x o で次のバッファへ移動
C-x 2 でバッファを分割
C-x 0 でバッファを閉じる
C-x o で次のバッファへ移動
C-x a でバッファ内でTerminalを起動

~/pp2/w14$ ./command.sh

## [w14.kp1] pyautoguiモジュールとマウスの制御 ##

# w14.kp1.1 マウスで操作するゲームの実行
Google Chromeを開いて
https://santatracker.google.com/intl/ja/presentbounce.html
にアクセスする

# w14.kp1.2 プログラムの実行（マウスを制御する）
~/pp2/w14$ cd kp1
~/pp2/w14/kp1$ ls

Filesを開く
-> ~/pp2/w14/kp1/input にある画像を確認する

~/pp2/w14/kp1$ ./command.sh

# w14.kp1.3 プログラムの確認
C-x C-f ~/pp2/w14/kp1/present_bounce.py

＊画像を見つけてクリックやドラッグするなど，マウスの制御方法を学ぶ

## [w14.kp2] キーボードの制御 ##

# w14.kp2.1 キーボードで操作するゲームの実行
~/pp2/w14/kp1$ cd ../kp2
~/pp2/w14/kp2$ ls
~/pp2/w14/kp2$ ./command.sh

＊プログラムの実行オプションを確認

~/pp2/w14/kp2$ ./command.sh play
~/pp2/w14/kp2$ tree

＊outputフォルダの中身を確認する

# w14.kp2.2 ゲームの確認，編集，再実行
C-x C-f ~/pp2/w14/kp2/app.py

＊着想の大体を捉える．絵画や彫刻におけるデッサンの初歩のイメージ．

~/pp2/w14/kp2$ ./command.sh edit

＊app.pyxresを書き換えて，鳥のくちばしを赤色に変える

~/pp2/w14/kp2$ ./command.sh play

# w14.kp2.3 プログラムの実行（キーボードを制御する）
~/pp2/w14/kp2$ ./command.sh autopilot

# w14.kp2.4 プログラムの確認
C-x C-f ~/pp2/w14/kp2/autopilot.py

＊右キーを押しながらスペースを押すなど，キーボードの制御方法を学ぶ

## [w14.kp3] フォーム画面で回答するプログラム ##

# w14.kp3.1 プログラムの実行
~/pp2/w14/kp2$ cd ../kp3
~/pp2/w14/kp3$ ls
~/pp2/w14/kp3$ ./command.sh

＊プログラムの実行オプションを確認

~/pp2/w14/kp3$ ./command.sh u1

＊1人目のデータがフォーム画面で回答されることを確認

~/pp2/w14/kp3$ ./command.sh u2

＊2人目のデータがフォーム画面で回答されることを確認

# w14.kp3.2 プログラムの確認
C-x C-f ~/pp2/w14/kp3/fill_out_form.py
