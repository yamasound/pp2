### 第5週 デバッグ (ver.0.1) ###

## [w05] 準備 ##

# w05.1 リポジトリの最新化
~$ cd pp2
~/pp2$ git pull

# w05.2 演習用ファイルの表示
~/pp2$ tree w05

# w01.3 README.mdの表示
~/pp2$ emacs -nw w05/README.md

## [w05.kp1] try / except / raise / assert 文によるエラーハンドリング ##

# w05.kp1.a1 プログラムの実行（boxの表示）
~/pp2/w05$ cd kp1_try_except_raise
~/pp2/w05/kp1_try_except_raise$ ls
~/pp2/w05/kp1_try_except_raise$ ./command.sh

# w05.kp1.a2 プログラムの表示
C-x 2 で バッファを縦分割
C-x o で 最も下のバッファへ移動
C-x C-f RET でDiredバッファを呼び出す
g で Diredバッファを最新化
box_print.py にカーソルを合わせて C-m
＊ プログラムと実行結果を見てもバグが見つからない
C-x 0 で バッファを閉じる

[Diredバッファのショートカット]
g     Diredバッファの最新化
　＊ カーソルの移動などはEmacsのショートカットと同じ
　＊ カーソルをファイルやディレクトリの上においてリターン（C-m）すると開く

# w05.kp1.a3 スクリーンバッファの作成
C-x o で README.md バッファへ移動
C-z c で スクリーンバッファを作成
C-z n で 次のスクリーンバッファへ移動
C-z n で 次のスクリーンバッファへ移動

# w05.kp1.a4 Pythonデバッガの起動
C-x C-b で 切り替え可能なバッファの表示
C-x o で *Buffer List* バッファへ移動
box_print.py にカーソルを合わせて C-m
C-x 1 で バッファを最大化
C-x 2 で バッファを縦分割
C-x o で 下のバッファへ移動
M-x pdb でPythonデバッガを起動
　python3 -m pdb box_print.py
　venvを用いる場合は
　~/venv/py3.10.12/bin/python3 -m pdb box_print.py

# w05.kp1.a5 Pythonデバッガの実行
n で現在の行を実行して次の行に移る
C-m 繰り返してプログラムを実行する
　＊ 何も入力せずにリターンすると，前と同じコマンドを繰り返す

[pdbのコマンド]
n(ext): 現在の行を実行して次の行へ移る
s(tep): 現在の行を実行して厳密な次の行へ移る（関数の中に入る）
p 変数: 変数をprintする
whatis 変数: 変数の型を表示する
r(eturn): 現在の関数が返るまで実行する
restart: デバッグ中のプログラムを再実行する
b(reak) [([filename:]lineno | function)] : ブレークポイントの追加
c(ontinue): 次のブレークポイントまで実行する
cl(er) bpnumber : ブレークポイントの削除
h(elp) : ヘルプ
q(uit): デバッグを終了する

# w05.kp1.a6 プログラムのデバッグ
C-x o で box_print.py のバッファへ移動
プログラムを修正
C-x C-s で プログラムを保存

C-x o で *gud-pdb* のバッファへ移動
デバッグモードでプログラムを実行

C-z n と C-x o で *ansi-term* のバッファへ移動
~/pp2/w05/kp1_try_except_raise$ ./command.sh

# w05.kp1.a7 不要なバッファの削除
C-z n で *gud-pdb* のバッファへ移動
C-x k で バッファを削除
C-z k で スクリーンバッファを削除

[Emacsのショートカット]
C-m リターン
C-z c スクリーンバッファの作成
C-z n スクリーンバッファの移動
C-z k スクリーンバッファの削除
C-x C-f RET Diredバッファの呼び出し
＊ g でバッファを最新化
＊ box_print.py を選択する
M-x pdb Pythonデバッガの起動
C-x k バッファの削除
＊ box_print.py と *gud-pdb* のバッファを削除する
C-x C-b 切り替え可能なバッファの表示
＊ g でバッファを最新化
＊ *ansi-term* を選択する

# w05.kp1.b1 プログラムの実行（信号機の色）
~/pp2/w05/kp1_try_except_raise$ cd ../kp1_assert
~/pp2/w05/kp1_assert$ ls
~/pp2/w05/kp1_assert$ ./command.sh

# w05.kp1.b2 Pythonデバッガによるデバッグ
・デバッグ用にスクリーンバッファを作成する
・traffic_signal.py を読み込んで pdb でデバッグする
・デバッグが完了したら *ansi-term* のバッファで実行結果を確かめる
・*gud-pdb* のバッファとデバッグ用のスクリーンバッファを削除する

## [w05.kp2] loggingモジュールによるロギング ##

# w05.kp2.1 プログラムの実行（階乗の計算）
~/pp2/w05/kp1_assert$ cd ../kp2
~/pp2/w05/kp2$ ls
~/pp2/w05/kp2$ ./command.sh
~/pp2/w05/kp2$ ./command.sh 5
＊ 5の階乗を計算すると，0が返る（計算結果が誤っている）

# w05.kp2.2 プログラムとログの確認
C-z c
C-x C-f RET
　~/pp2/w05/kp2/factorial.py を呼び出す
C-x 2
C-x a
~/pp2/w05/kp2$ cat output/log.txt

# w05.kp2.3 ログを見ながらプログラムをデバッグ
~/pp2/w05/kp2$ ./command.sh 5 DEBUG; cat output/log.txt
＊ 5の階乗を計算して，120が返るようにプログラムを修正

## [w05.kp3] 足し算プログラムのデバッグ ##

# w05.kp3.1 プログラムの実行（足し算）
~/pp2/w05/kp2$ cd ../kp3
~/pp2/w05/kp3$ ls
~/pp2/w05/kp3$ ./command.sh
＊ 1と2と3を足すと，123が返る（計算結果が誤っている）

# w05.kp3.2 プログラムと途中経過を表示しながらデバッグ
C-x C-f ~/pp2/w05/kp3/add.py

~/pp2/w05/kp3$ ./command.sh
＊ 1と2と3を足して，6が返るようにプログラムを修正

[Emacsのショートカット]
M-x replace-regexp 正規表現を用いた置換

＊ ヒント1
　 assert first == 1
　 とすると「第1の数」として入力した値が1か確認できる

＊ ヒント2
　 print(type(変数))
　 とすると，変数の型を表示できる
