import os
import time
import consts
import jieba

from . import utils

path = os.path.dirname(__file__)


def in_charset(word: str):
    for char in consts.charset:
        if char in word:
            return True
    return False


with open(path+"/words.txt", "r") as f:
    words = dict((x.split(" ")[0], int(x.split(" ")[1])) for x in f.read().rstrip("\n").split("\n") if in_charset(x))


# print(words)

def learn_from_id(pid: int, encrypt_method: str = "none"):
    try:
        p = utils.get_cdycc(pid)

        for block in jieba.cut(p):
            if in_charset(block):
                if block not in words:
                    words[block] = 0
                words[block] += 1
        with open(path+"/words.txt", "w") as f:
            f.writelines(f"{x} {y}\n" for x, y in words.items())
        # print(pid)
    except Exception as e:
        print(e)
        time.sleep(5)


if __name__ == '__main__':
    learn_from_id(5929, "none")
