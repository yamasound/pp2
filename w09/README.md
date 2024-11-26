### 第9週 Excelスプレッドシートの操作 (ver.0.1) ###

## [w09] 準備 ##

# w09.1 リポジトリの最新化
~$ cd pp2
~/pp2$ git pull

# w09.2 演習用ファイルの表示
~/pp2$ tree w09

# w09.3 README.mdの表示
~/pp2$ emacs -nw w09/README.md

## [w09.kp1] openpyxlモジュールとWorkbookオブジェクト ##

# w09.kp1.1 プログラムの実行（複数のファイルを纏めてスプレッドシートを作る）
~/pp2/w09$ cd kp1
~/pp2/w09/kp1$ ls
~/pp2/w09/kp1$ ./command.sh

# w09.kp1.2 テキストファイルの確認
Filesで ~/pp2/w09/kp1/output/txt/d01.txt から d05.txt を開く

# w09.kp1.3 プログラムの確認
C-x C-f ~/pp2/w09/kp1/generate_texts.py
C-x C-f ~/pp2/w09/kp1/texts_to_xlsx.py

## [w09.kp2] スプレッドシートの行と列の値の入れ替え ##

# w09.kp2.1 プログラムの実行（スプレッドシートを操作する）
~/pp2/w09/kp1$ cd ../kp2
~/pp2/w09/kp2$ ls
~/pp2/w09/kp2$ ls input
~/pp2/w09/kp2$ ./command.sh

# w09.kp2.2 スプレッドシートの確認
Filesで ~/pp2/w09/kp2/input/texts.xlsx を開く

# w09.kp2.3 プログラムの確認
C-x C-f ~/pp2/w09/kp2/swap_rows_and_cols.py

## [w09.kp3] 複数のスプレッドシートの一括操作 ##

# w09.kp3.1 プログラムの実行（見積書，納品書，請求書を発行する）
~/pp2/w09/kp2$ cd ../kp3
~/pp2/w09/kp3$ ls
~/pp2/w09/kp3$ ls input
~/pp2/w09/kp3$ ./command.sh

# w09.kp3.2 雛形の確認
LibreOffice Calcで ~/pp2/w09/kp3/input/template.xlsx を開く

# w09.kp3.3 プログラムの確認
C-x C-f ~/pp2/w09/kp3/issue_documents.py
