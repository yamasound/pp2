#!/usr/bin/env python3

import os, re
from pathlib import Path

def read_form(path_input):
    with open(path_input, 'r') as fi:
        form = fi.read()
    return form

def write_sentence(sentence, path_output):
    os.makedirs(path_output.parent)
    with open(path_output, 'w') as fo:
        fo.write(sentence)

def replace_words(form):
    pattern = re.compile(r'(形容詞|名詞|動詞|形容動詞|副詞)')
    while True:
        mo = pattern.search(form)
        if not mo:
            break
        repl = input(f"{mo.group(1)}を入力してください: ")
        form = form.replace(mo.group(1), repl, 1)
    print(form, end='')
    return form

def main(file_input, file_output):
    form = read_form(file_input)
    sentence = replace_words(form)
    write_sentence(sentence, file_output)

if __name__ == '__main__':
    path_input = Path('input', 'form.txt')
    path_output = Path('output', 'sentence.txt')
    main(path_input, path_output)
