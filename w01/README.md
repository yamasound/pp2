### 第1週 PDFとWord文書の操作 (ver.0.1) ###

## [w01] 準備 ##

# w01.1 リポジトリのクローン
Terminalを開く（Terminalでの操作は$で示す．$の前はディレクトリを表す）
~$ rm -rf ~/pp2
~$ cd; git clone github:yamasound/pp2

# w01.2 演習用ファイルの表示
~$ tree pp2/w01

# w01.3 README.mdの表示
~$ emacs -nw pp2/w01/README.md

[Emacsのショートカット]
C-n で下へ移動
C-p で上へ移動
C-f で右へ移動
C-b で左へ移動
C-a で行頭へ移動
C-x C-c で終了

[Terminalのショートカット]
C-p で前のコマンドを表示
C-n で次のコマンドを表示

~$ emacs -nw pp2/w01/README.md

# w01.4 ライブラリのインストール
[Emacsのショートカット]
C-x 2 でバッファを分割
C-x o で次のバッファへ移動
C-x a でバッファ内でTerminalを起動

~/pp2/w01$ ./command.sh

## [w01.kp1] PyPDF2 モジュールによる PDF の操作 ##

# w01.kp1.1 入力ファイルの確認
FilesでHome -> pp2 -> w01 -> kp1 -> input -> a.pdfとb.pdfの内容を確認する

# w01.kp1.2 プログラムの実行
~/pp2/w01$ cd kp1
~/pp2/w01/kp1$ ls
~/pp2/w01/kp1$ ./command.sh
all.pdfのウィンドウを閉じる（右上のx印をクリック）

# w01.kp1.3 出力ファイルの確認
~/pp2/w01/kp1$ ls
~/pp2/w01/kp1$ ls output
~/pp2/w01/kp1$ evince output/all.pdf
FilesでHome -> pp2 -> w01 -> kp1 -> output -> all.pdfの内容を確認する

# w01.kp1.4 プログラムの確認
C-x C-f ~/pp2/w01/kp1/join_pdfs.py
C-x k RET

# w01.kp1.5 出力ファイルの削除
~/pp2/w01/kp1$ ls
~/pp2/w01/kp1$ ./clean.sh
~/pp2/w01/kp1$ ls

## [w01.kp2] docx モジュールによる Word 文書の操作 ##

# w01.kp2.1 プログラムの確認
~/pp2/w01/kp1$ cd ../kp2
~/pp2/w01/kp2$ ls
C-x C-f ~/pp2/w01/kp2/make_invitation.py
C-x k RET

# w01.kp2.2 プログラムの実行
~/pp2/w01/kp2$ ./command.sh

# w01.kp2.3 出力ファイルの確認
~/pp2/w01/kp2$ ls
~/pp2/w01/kp2$ ls output
~/pp2/w01/kp2$ libreoffice --nologo --writer output/invitation.docx
FilesでHome -> pp2 -> w01 -> kp2 -> output -> invitation.docxの内容を確認する

# w01.kp2.4 出力ファイルの削除
~/pp2/w01/kp2$ ls
~/pp2/w01/kp2$ ./clean.sh
~/pp2/w01/kp2$ ls

## [w01.kp3] 複数の招待者に対して個別に招待状を作成するプログラム ##

# w01.kp3.1 入力ファイルの確認
FilesでHome -> pp2 -> w01 -> kp3 -> input -> guest.txtの内容を確認する
~/pp2/w01/kp2$ cd ../kp3
~/pp2/w01/kp3$ ls
~/pp2/w01/kp3$ ls input
~/pp2/w01/kp3$ cat input/guests.txt

# w01.kp3.2 プログラムの確認
C-x C-f ~/pp2/w01/kp3/make_invitations.py
C-x k RET

# w01.kp3.3 プログラムの実行
~/pp2/w01/kp3$ ./command.sh

# w01.kp3.4 出力ファイルの確認
~/pp2/w01/kp3$ ls
~/pp2/w01/kp3$ ls output
~/pp2/w01/kp3$ libreoffice --nologo --writer output/invitations.docx
FilesでHome -> pp2 -> w01 -> kp3 -> output -> invitations.docxの内容を確認する

# w01.kp3.5 入力ファイルの編集（秋田太郎を秋田花子に変更する）
C-x C-f ~/pp2/w01/kp3/input/guests.txt
C-f を2回押してカーソルを右へ2つ移動する
C-k でカーソル以降を削除する
Shift + Space を押して日本語入力モードにする
花子と入力する
Shift + Space を押して英語入力モードに戻す
C-x C-s で保存する
C-x k RET でバッファを削除する

# w01.kp3.6 入力ファイルの確認
~/pp2/w01/kp3$ cat input/guests.txt

# w01.kp3.7 プログラムの再実行
~/pp2/w01/kp3$ ./command.sh

# w01.kp3.8 出力ファイルの削除
~/pp2/w01/kp3$ ls
~/pp2/w01/kp3$ ./clean.sh
~/pp2/w01/kp3$ ls
