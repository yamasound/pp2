### 第8週 ファイル管理 (ver.0.1) ###

## [w08] 準備 ##

# w08.1 リポジトリの最新化
~$ cd pp2
~/pp2$ git pull

# w08.2 演習用ファイルの表示
~/pp2$ tree w08

# w08.3 README.mdの表示
~/pp2$ emacs -nw w08/README.md

## [w08.kp1] shutilモジュールによるファイルの操作 ##

# w08.kp1.1 プログラムの実行（条件に合うファイルを選び出す）
~/pp2/w08$ cd kp1
~/pp2/w08/kp1$ ls
~/pp2/w08/kp1$ tree input
~/pp2/w08/kp1$ ./command.sh
~/pp2/w08/kp1$ ./command.sh txt 1
~/pp2/w08/kp1$ ./command.sh jpg 100
~/pp2/w08/kp1$ ./command.sh jpg 1000

# w08.kp1.2 プログラムの確認
C-x C-f ~/pp2/w08/kp1/select_copy.py

## [w08.kp2] zipfileモジュールによるファイルの圧縮 ##

# w08.kp2.1 プログラムの実行（ファイルとディレクトリを復元する）
~/pp2/w08/kp1$ cd ../kp2
~/pp2/w08/kp2$ ls
~/pp2/w08/kp2$ ./clean.sh
~/pp2/w08/kp2$ ./command.sh
~/pp2/w08/kp2$ rm -rf output/data/sub; tree output
~/pp2/w08/kp2$ ./command.sh 1

# w08.kp2.2 プログラムの確認
C-x C-f ~/pp2/w08/kp2/clean.sh
C-x C-f ~/pp2/w08/kp2/generate_data.py
C-x C-f ~/pp2/w08/kp2/command.sh
C-x C-f ~/pp2/w08/kp2/snapshot.py

## [w08.kp3] ディレクトリのスナップショットを世代管理するプログラム ##

# w08.kp3.1 プログラムの実行（ファイルとディレクトリを任意の時点に復元する）
~/pp2/w08/kp2$ cd ../kp3
~/pp2/w08/kp3$ ls
~/pp2/w08/kp3$ ./clean.sh
~/pp2/w08/kp3$ ./command.sh
~/pp2/w08/kp3$ rm -rf output/data/sub; tree output
~/pp2/w08/kp3$ ./command.sh
~/pp2/w08/kp3$ ./command.sh 1
~/pp2/w08/kp3$ ./command.sh 2

# w08.kp3.2 プログラムの確認
C-x C-f ~/pp2/w08/kp3/generational_snapshot.py
