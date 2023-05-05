import time
import consts
import jieba

import utils


def in_charset(word: str):
    for char in consts.charset:
        if char in word:
            return True
    return False


with open("words.txt", "r") as f:
    words = dict((x.split(" ")[0], int(x.split(" ")[1])) for x in f.read().rstrip("\n").split("\n") if in_charset(x))

# print(words)

for x in range(482, 4896):
    try:
        p = utils.get_cdycc(x)

        for block in jieba.cut(p):
            if in_charset(block):
                if block not in words:
                    words[block] = 0
                words[block] += 1
        with open("words.txt", "w") as f:
            f.writelines(f"{x} {y}\n" for x, y in words.items())
        print(x)
    except Exception as e:
        print(e)
        time.sleep(5)
