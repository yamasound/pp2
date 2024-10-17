### 第4週 ファイルの読み書き (ver.0.1) ###

## [w04] 準備 ##

# w04.1 リポジトリの最新化
~$ cd pp2
~/pp2$ git pull

# w04.2 演習用ファイルの表示
~/pp2$ tree w04

# w01.3 README.mdの表示
~/pp2$ emacs -nw w04/README.md

## [w04.kp1] pathlibモジュールとPathオブジェクトによるファイルの指定 ##

# w04.kp1.1 プログラムの実行（pngファイルの整理）
~/pp2/w04$ cd kp1
~/pp2/w04/kp1$ ls
~/pp2/w04/kp1$ tree input; ./command.sh png; tree output

[Emacsのショートカット（復習）]
C-c C-j lineモードへの移行
C-c C-k charモードへの移行
C-p カーソルを上へ移動
C-f カーソルを右へ移動
C-b カーソルを左へ移動
C-n カーソルを下へ移動
C-x o カーソルを次のバッファへ移動
C-x 2 バッファを縦分割
C-x k RET バッファを削除

[Emacsのショートカット]
C-k カーソル位置から行末までカット
C-y ペースト
C-r 後方検索
C-s 前方検索
C-g 中止
C-a カーソルを行頭へ移動
C-e カーソルを行末へ移動
M-< カーソルを一番上へ移動
M-> カーソルを一番下へ移動
C-SPC カーソル位置にマークをセット
C-w マークからカーソル位置までカット
M-w マークからカーソル位置までコピー
C-x u アンドゥ
C-x p カーソルを前のバッファへ移動
C-x 0 バッファを閉じる
C-x 1 バッファを最大化
C-x b バッファを呼び出す

# w04.kp1.2 プログラムを確認しながら実行
C-x 2 でバッファを縦分割
C-x 0 でバッファを閉じる

C-x o で上のバッファへ移動
C-x 2 でバッファを縦分割
C-x o で中間のバッファへ移動
C-x C-f ~/pp2/w04/kp1/align_files.py

C-x o で下のバッファへ移動
~/pp2/w04/kp1$ tree input; ./command.sh png,jpg; tree output
~/pp2/w04/kp1$ tree input; ./command.sh png,jpg,jpeg; tree output
~/pp2/w04/kp1$ ./clean.sh; ls

＊以降はカーソルやバッファを操作するショートカットの記載を省略します．

## [w04.kp2] with / open 文によるファイルの読み書き ##

# w04.kp2.1 入力データの確認とプログラムの実行
~/pp2/w04/kp1$ cd ../kp2
~/pp2/w04/kp2$ ls
~/pp2/w04/kp2$ cat input/form.txt
~/pp2/w04/kp2$ ./command.sh

# w04.kp2.2 プログラムと出力データの確認
C-x C-f ~/pp2/w04/kp2/sentence_generator.py

~/pp2/w04/kp2$ cat output/sentence.txt
~/pp2/w04/kp2$ ./clean.sh; ls

## [w04.kp3] 更新可能なマルチクリップボードのプログラム ##

# w04.kp3.1 プログラムの実行
~/pp2/w04/kp2$ cd ../kp3
~/pp2/w04/kp3$ ls
~/pp2/w04/kp3$ ./command.sh

# w04.kp3.2 プログラムを確認しながら実行
C-x C-f ~/pp2/w04/kp3/multi_clipboard.py

~/pp2/w04/kp3$ ./command.sh
Text Editorを起動して，クリップボードの内容をペーストする

Text Editorに a1 と書いた行を作り，クリップボードにコピーする
~/pp2/w04/kp3$ ./command.sh save a
Text Editorにクリップボードの内容をペーストする

Text Editorに b1,b2 と書いた行を作り，クリップボードにコピーする
~/pp2/w04/kp3$ ./command.sh save b
Text Editorにクリップボードの内容をペーストする

Text Editorに c1,c2,c3 と書いた行を作り，クリップボードにコピーする
~/pp2/w04/kp3$ ./command.sh save c
Text Editorにクリップボードの内容をペーストする

~/pp2/w04/kp3$ ./command.sh load a
Text Editorにクリップボードの内容をペーストする

~/pp2/w04/kp3$ ./command.sh load b
Text Editorにクリップボードの内容をペーストする

~/pp2/w04/kp3$ ./command.sh load c
Text Editorにクリップボードの内容をペーストする

~/pp2/w04/kp3$ ./command.sh delete a
Text Editorにクリップボードの内容をペーストする

~/pp2/w04/kp3$ ./command.sh delete all
Text Editorにクリップボードの内容をペーストする

# w04.kp3.3 出力ファイルの確認と削除
~/pp2/w04/kp3$ ls
~/pp2/w04/kp3$ tree output
~/pp2/w04/kp3$ ./clean.sh
~/pp2/w04/kp3$ ls
