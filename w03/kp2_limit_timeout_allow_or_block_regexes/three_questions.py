#!/usr/bin/env python3

import pyinputplus as pyip
import random, time

def question(question_number, correct_answers):
    # ランダムに2つの数字を選ぶ
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = f"#{question_number}: {num1} x {num2} = "

    try:
        # 正答を allowRegexes で扱い、誤答を blockRegexes で扱う
        pyip.inputStr(prompt, limit=2, timeout=5,
                      allowRegexes=[f"^{num1 * num2}$"],
                      blockRegexes=[('.*', '不正解!')])
                      
    except pyip.RetryLimitException:
        print('回数制限を超えました!')
    except pyip.TimeoutException:
        print('時間制限を超えました!')
    else:
        # tryブロックで例外が起こらなければ、このブロックが実行される
        print('正解!')
        correct_answers += 1
    return correct_answers

def main(questions):
    correct_answers = 0
    for question_number in range(1, questions + 1):
        correct_answers = question(question_number, correct_answers)
        time.sleep(1) # ユーザーが結果を読めるように小休止
        
    ratio = int(100 * correct_answers / question_number)
    print(f"正解率: {ratio}%")

if __name__ == "__main__":
    main(questions=3)
