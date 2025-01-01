### 第13週 時間管理，タスクのスケジューリング，プログラム起動 (ver.0.1) ###

## [w13] 準備 ##

# w13.1 リポジトリの最新化
~$ cd pp2
~/pp2$ git pull

# w13.2 演習用ファイルの表示
~/pp2$ tree w13

# w13.3 README.mdの表示
~/pp2$ emacs -nw w13/README.md

# w13.4 パッケージのインストール
C-x 2 でバッファを分割
C-x o で次のバッファへ移動
C-x 2 でバッファを分割
C-x 0 でバッファを閉じる
C-x o で次のバッファへ移動
C-x a でバッファ内でTerminalを起動

~/pp2/w13$ ./command.sh

## [w13.kp1] datetime モジュールによる時間管理 ##

# w13.kp1.1 プログラムの実行（使用中の計算機の時刻の誤差を調べる）
~/pp2/w13$ cd kp1
~/pp2/w13/kp1$ ls
~/pp2/w13/kp1$ ./command.sh

＊NICT（エヌアイシーティー）は
  国立研究開発法人情報通信研究機構
  National Institute of Information and Communications Technology
  の略称であり，日本標準時を決定している

＊日本標準時（JST: Japan Standard Time）は
  協定世界時（UTC: Coordinated Universal Time）より
  9時間早い

# w13.kp1.2 プログラムの確認
C-x C-f ~/pp2/w13/kp1/clock.py

## [w13.kp2] threading / subprocess モジュールによる並行 / 並列 処理 ##

# w13.kp2.1 プログラムの実行（親プロセスからスレッドとサブプロセスを実行する）
~/pp2/w13/kp1$ cd ../kp2
~/pp2/w13/kp2$ ls
~/pp2/w13/kp2$ ./command.sh

＊プログラムの実行オプションを確認

~/pp2/w13/kp2$ ./command.sh worker.py th

＊Method Resolution Order に threading のクラスがあることを確認

＊4秒間経過したらプログラムが終了することを確認

~/pp2/w13/kp2$ ./command.sh worker.py mp

＊Method Resolution Order に multiprocessing のクラスがあることを確認

＊4秒間経過したらプログラムが終了することを確認

＊並行処理は切り替えながら処理をする．並列処理は同時に処理をする．
　すなわち，2並行よりも2並列は2倍多く（または2倍早く）処理できる

# w13.kp2.2 プログラムの確認，変更，実行（処理の親子関係を設定する）
C-x C-f ~/pp2/w13/kp2/worker.py

プログラムにあるdaemonをFalseに設定を変更する

~/pp2/w13/kp2$ ./command.sh worker.py th

＊4秒間経過してもプログラムが終了しないことを確認
　（親プロセスが終了しても子は独立して動き続ける）

Emacsのansi-termのバッファへ移動する
-> C-c C-c でプログラムを終了する

~/pp2/w13/kp2$ ./command.sh worker.py mp

＊4秒間経過してもプログラムが終了しないことを確認
　（親プロセスが終了しても子は独立して動き続ける）

Emacsのansi-termのバッファへ移動する
-> C-c C-c でプログラムを終了する

プログラムにあるdaemonをTrueに設定を戻す

# w13.kp2.3 プログラムの実行（並行処理の結果を表示する）
~/pp2/w13/kp2$ ./command.sh st_clock.py th

＊初回のみEmailの入力を求められるが，何も入力せずにEnterキーを押す

自動でChromeのタブが開く
-> "Start worker"ボタンをクリック
-> "Worker thread"と表示されて，10秒間時刻が更新される
-> "Stop worker"ボタンをクリック

Emacsのansi-termのバッファへ移動する
-> C-c C-c でプログラムを終了する

# w13.kp2.4 プログラムの実行（並列処理の結果を表示する）
~/pp2/w13/kp2$ ./command.sh st_clock.py mp

自動でChromeのタブが開く
-> "Start worker"ボタンをクリック
-> "Worker process"と表示されて，10秒間時刻が更新される
-> "Stop worker"ボタンをクリック

Emacsのansi-termのバッファへ移動する
-> C-c C-c でプログラムを終了する

# w13.kp2.5 プログラムの実行（workerが処理を行うプロセスを確認する）
~/pp2/w13/kp2$ ./command.sh st_clock.py th

Terminalを起動 ->
ps a | grep python3 | grep clock

＊プロセスは1つしか割り当てられていないことを確認
　（workerの処理は親プロセスの中にあるスレッドで行われている）

Emacsのansi-termのバッファへ移動する
-> C-c C-c でプログラムを終了する

~/pp2/w13/kp2$ ./command.sh st_clock.py mp

（上で起動した）Terminalを選択 ->
ps a | grep python3 | grep clock

pstree -p (streamlitのプロセス番号)

＊プロセスが2つ割り当てられていることを確認
　（workerの処理は親プロセスの配下にあるサブプロセスで行われている）

# w13.kp2.6 プログラムの確認
C-x C-f ~/pp2/w13/kp2/st_clock.py

## [w13.kp3] 天気予報データを定期的に更新するプログラム ##

# w13.kp3.1 プログラムの実行（秋田の天気予報のデータを取得する）
~/pp2/w13/kp2$ cd ../kp3
~/pp2/w13/kp3$ ls

＊csv_io.py, json_io.py, weather_html.pyはw12と同じ

~/pp2/w13/kp3$ ./command.sh
~/pp2/w13/kp3$ ./command.sh weather_data.py

Filesを起動
-> ~/pp2/w13/kp3/output 以下を確認

＊秋田の天気予報のデータが取得できていることを確認

# w13.kp3.2 プログラムの確認
C-x C-f ~/pp2/w13/kp3/weather_data.py

# w13.kp3.3 プログラムの実行（各地の天気予報のデータを取得して表示する）
~/pp2/w13/kp3$ ./command.sh st_weather.py th

＊秋田，東京，那覇の天気予報のデータを取得して表示できていることを確認

~/pp2/w13/kp3$ ./command.sh st_weather.py mp

＊取得する地域やデータが多くなれば並列処理の効果が発揮される

# w13.kp3.4 プログラムの確認
C-x C-f ~/pp2/w13/kp3/st_weather.py
