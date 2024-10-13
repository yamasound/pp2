#!/usr/bin/env python3

import sys, time
sys.path.append('..')
from kp2_limit_timeout_allow_or_block_regexes.three_questions import question

def main(correct_answers_for_goal):
    question_number = 0
    correct_answers = 0
    while correct_answers < correct_answers_for_goal:
        question_number += 1
        correct_answers = question(question_number, correct_answers)
        time.sleep(1)

    ratio = int(100 * correct_answers / question_number)
    print(f"3問正解しました！正解率: {ratio}%")
    
if __name__ == "__main__":
    main(correct_answers_for_goal=3)
