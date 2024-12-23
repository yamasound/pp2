### 第12週 CSV ファイルと JSON データの操作 (ver.0.1) ###

## [w12] 準備 ##

# w12.1 リポジトリの最新化
~$ cd pp2
~/pp2$ git pull

# w12.2 演習用ファイルの表示
~/pp2$ tree w12

# w12.3 README.mdの表示
~/pp2$ emacs -nw w12/README.md

# w12.4 パッケージのインストール
C-x 2 でバッファを分割
C-x o で次のバッファへ移動
C-x a でバッファ内でTerminalを起動

~/pp2/w12$ ./command.sh

## [w12.kp1] csvモジュールによるCSVファイルの操作 ##

# w12.kp1.1 プログラムの実行（CSVファイルを読み書きする）
~/pp2/w12$ cd kp1
~/pp2/w12/kp1$ ls
~/pp2/w12/kp1$ ./command.sh
~/pp2/w12/kp1$ tree output
~/pp2/w12/kp1$ cat output/code_and_city.csv

# w12.kp1.2 プログラムの確認
C-x C-f ~/pp2/w12/kp1/csv_io.py

## [w12.kp2] jsonモジュールによるJSONデータの操作 ##

# w12.kp2.1 プログラムの実行（JSONデータを読み書きする）
~/pp2/w12/kp1$ cd ../kp2
~/pp2/w12/kp2$ ls
~/pp2/w12/kp2$ tree input
~/pp2/w12/kp2$ cat input/sample.json
~/pp2/w12/kp2$ ./command.sh
~/pp2/w12/kp2$ tree output
~/pp2/w12/kp2$ diff input/sample.json output/sample.json
~/pp2/w12/kp2$ cat output/sample.csv 

# w12.kp2.2 プログラムの実行（秋田の天気予報のデータを取得する）
~/pp2/w12/kp2$ ./command.sh 秋田

# w12.kp2.3 プログラムの確認
C-x C-f ~/pp2/w12/kp2/json_io.py

## [w12.kp3] 現在の天気予報データを取得するプログラム ##

# w12.kp3.1 プログラムの実行（各地の天気予報のデータを取得して表示する）
~/pp2/w12/kp2$ cd ../kp3
~/pp2/w12/kp3$ ls
~/pp2/w12/kp3$ tree input
~/pp2/w12/kp3$ less input/template.html
~/pp2/w12/kp3$ ./command.sh 秋田 東京 那覇
~/pp2/w12/kp3$ tree output
~/pp2/w12/kp3$ chromium output/weather/秋田.html output/weather/東京.html output/weather/那覇.html

# w12.kp3.2 プログラムの確認
C-x C-f ~/pp2/w12/kp3/weather_html.py
