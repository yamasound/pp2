### 第7週 画像の操作 (ver.0.1) ###

## [w07] 準備 ##

# w07.1 リポジトリの最新化
~$ cd pp2
~/pp2$ git pull

# w07.2 演習用ファイルの表示
~/pp2$ tree w07

# w07.3 README.mdの表示
~/pp2$ emacs -nw w07/README.md

## [w07.kp1] PILモジュールとImageクラス ##

# w07.kp1.1 プログラムの実行と確認（Fontイメージを表示する）
~/pp2/w07$ cd kp1
~/pp2/w07/kp1$ ls
~/pp2/w07/kp1$ ./command.sh

0番のスクリーンバッファの下部へ移動する
C-c C-c で中止

~/pp2/w07/kp1$ ls
~/pp2/w07/kp1$ ls output

# w07.kp1.2 プログラムの表示
C-z c で スクリーンバッファを作成
C-x C-b で 切り替え可能なバッファの表示
C-x o で *Buffer List* バッファへ移動
*ansi-term* にカーソルを合わせて C-m
C-x 2 で バッファを分割
C-x 0 で バッファを閉じる
C-x o で 上のバッファへ移動
C-x C-f ~/pp2/w07/kp1/create_font_images.py
C-z n で スクリーンバッファを移動

## [w07.kp2] 画像の操作 ##

# w07.kp2.1 プログラムの実行と確認（ロゴを画像に追加する）
~/pp2/w07/kp1$ cd ../kp2
~/pp2/w07/kp2$ ls
~/pp2/w07/kp2$ ./command.sh

0番のスクリーンバッファの下部へ移動する
C-c C-c で中止

~/pp2/w07/kp2$ ls
~/pp2/w07/kp2$ ls output

# w07.kp2.2 プログラムの表示
1番のスクリーンバッファの上部へ移動する
C-x C-f ~/pp2/w07/kp2/add_logo_to_images.py

## [w07.kp3] 複数の出席者に対して個別に席札を作成するプログラム ##

# w07.kp3.1 プログラムの実行（文字と画像を含む席札を作成する）
~/pp2/w07/kp2$ cd ../kp3
~/pp2/w07/kp3$ ls
~/pp2/w07/kp3$ ./command.sh

0番のスクリーンバッファの下部へ移動する
C-c C-c で中止

~/pp2/w07/kp3$ ls
~/pp2/w07/kp3$ ls output

# w07.kp3.2 プログラムの確認
1番のスクリーンバッファの上部のバッファへ移動
C-x C-f ~/pp2/w07/kp3/create_place_cards.py
