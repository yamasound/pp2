### 第3週 入力検証 (ver.0.1) ###

## [w03] 準備 ##

# w03.1 リポジトリの最新化
~$ cd pp2
~/pp2$ git pull

# w03.2 演習用ファイルの表示
~/pp2$ tree w03

# w01.3 README.mdの表示
~/pp2$ emacs -nw w03/README.md

## [w03.kp1] pyinputplusモジュールによる入力検証 ##

# w03.kp1.1 プログラムの実行
~/pp2/w03$ cd kp1
~/pp2/w03/kp1$ ls
~/pp2/w03/kp1$ ./command.sh

# w03.kp1.2 プログラムの確認（実行結果を見ながら）
C-x o で上のバッファへ移動
C-x C-f ~/pp2/w03/kp1/tease.py
C-x k RET

## [w03.kp2] min, max, limit, timeout, allow / block Regexes オプション ##

# w03.kp2.a1 プログラムの実行
C-x o で下のバッファへ移動
~/pp2/w03/kp1$ cd ../kp2_min_max
~/pp2/w03/kp2_min_max$ ls
~/pp2/w03/kp2_min_max$ ./command.sh

# w03.kp2.a2 プログラムの確認
C-x o で上のバッファへ移動
C-x C-f ~/pp2/w03/kp2_min_max/sandwich.py
C-x k RET

# w03.kp2.b1 プログラムの実行
~/pp2/w03/kp2__min_max$ cd ../kp2_limit_timeout_allow_or_block_regexes
~/pp2/w03/kp2_limit_timeout_allow_or_block_regexes$ ls
~/pp2/w03/kp2_limit_timeout_allow_or_block_regexes$ ./command.sh

[質問への入力が検証される]
・2回間違えるとその質問は間違いとなる
・5秒経過するとその質問は時間切れとなる
・掛け算の答えが合えば正解となり，それ以外は不正解となる

# w03.kp2.b2 プログラムの確認
C-x o で上のバッファへ移動
C-x C-f ~/pp2/w03/kp2_limit_timeout_allow_or_block_regexes/three_questions.py 
C-x k RET

[質問のプログラムを再利用できるように関数で書いておく]
def question(question_number, correct_answers):
    ...
    return correct_answers

[メインで呼ばれた場合にのみmain関数を実行する]
if __name__ == "__main__":
    main(questions=3)

## [w03.kp3] 掛け算クイズのプログラム ##

# w03.kp3.1 プログラムの実行
C-x o で下のバッファへ移動
~/pp2/w03/kp2_limit_timeout_allow_or_block_regexes$ cd ../kp3
~/pp2/w03/kp3$ ls
~/pp2/w03/kp3$ ./command.sh

# w03.kp3.2 プログラムの確認
C-x o で上のバッファへ移動
C-x C-f ~/pp2/w03/kp3/continue_until_three_questions_are_answered_correctly.py
C-x k RET

[質問のプログラムを再利用する]
sys.path.append('..')
from kp2_limit_timeout_allow_or_block_regexes.three_questions import question
