# 本项目不保证后续开发

鉴于
[C的云存储](http://mp.weixin.qq.com/profile?src=3&timestamp=1685724428&ver=1&signature=7aX47yuLgfUkD8Svf3OTJIfL1kDRq1T2R-7kv3utqF0hFsn49dRHWMbAs-P4K2VES5TXJ1PmIEL3n4nvxMjNVw==)
[遭到了恶意举报](https://mp.weixin.qq.com/s?src=11&timestamp=1685724428&ver=4566&signature=sHBp-x1jHGRp79o*-vZYNn56PYe1uaBbjkzWRW7WQHfaDSnzeT5xawzylKxkJ3kLwT1NmytwamWhg7Yo2JooeHmZyYvKUumC9I13igv2v9QHK8kajXH3zA4QtRbF0d7A&new=1)
(这年头为爱发电真tm难md)
而且几乎没人用本项目，我们将随时考虑无限期放弃该项目的后续开发（当然欢迎接手awa）

如果有人在用这个项目，或者愿意加入开发，欢迎告诉我们 :)

# zhihuDecrypt

## 欢迎你, 可以给我一颗星星吗?

用于识别与解密部分文章的Python包

---

## 声明

1. 本项目不提供任何采集知乎内容的方法或技术
2. 仅作学习文本分析用途，请勿用于侵犯他人利益 :)
3. 代码很粗糙，欢迎PR :)
4. 大部分代码没写注释，我懒 :(
5. 本项目在GPLv3下授权，欢迎各位在遵循许可的情况下继续开发

## 原理

### 字体来源

见此[聊聊知乎盐选反爬 (回答页篇) - 创新者.老王的博客](https://blog.cxzlw.top/2023/07/05/zhihu-aac-old/)

## 用法

1. `poetry add git+https://github.com/cxzlw/zhihuDecrypt`
2. `import zhihudecrypt`
3. 参考[zhihuDecryptApp](https://github.com/cxzlw/zhihuDecryptApp)

## words.txt 的来源

通过以下代码，注意通过`learn_from_id()`收集的文章越多越好

若传入的`id`指向了一篇乱码文章，注意传入对应的解密方法，或者只传入正常文章

```python
import os
import time
import consts
import jieba
import httpx

from bs4 import BeautifulSoup

path = os.path.dirname(__file__)


def get_cdycc(passage_id: int):
    html = httpx.get(f"https://cdycc.cn/?id={passage_id}")
    soup = BeautifulSoup(html, "html5lib")
    selected = soup.select(
        "body > div.wrapper > div.main.fixed > div.wrap > div.content > div:nth-child(1) > div.post > "
        "div.single.postcon > div.readall-body > p")
    return "\n".join(x.text for x in selected[2:-3])


def in_charset(word: str):
    for char in consts.charset:
        if char in word:
            return True
    return False


with open(path + "/words.txt", "r") as f:
    words = dict((x.split(" ")[0], int(x.split(" ")[1])) for x in f.read().rstrip("\n").split("\n") if in_charset(x))


# print(words)

def learn_from_id(pid: int, encrypt_method: str = "none"):
    try:
        p = get_cdycc(pid)

        for block in jieba.cut(p):
            if in_charset(block):
                if block not in words:
                    words[block] = 0
                words[block] += 1
        with open(path + "/words.txt", "w") as f:
            f.writelines(f"{x} {y}\n" for x, y in words.items())
        # print(pid)
    except Exception as e:
        print(e)
        time.sleep(5)


if __name__ == '__main__':
    learn_from_id(5929, "none")
```

## 推荐网站

### 不对该网站内容负责，请自行评估

[C的云存储](https://cdycc.cn/)
[创新者.老王的博客](https://blog.cxzlw.top/)
