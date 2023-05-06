import httpx
import consts

from bs4 import BeautifulSoup


def get_cdycc(passage_id: int):
    html = httpx.get(f"https://cdycc.cn/?id={passage_id}")
    soup = BeautifulSoup(html, "html5lib")
    selected = soup.select(
        "body > div.wrapper > div.main.fixed > div.wrap > div.content > div:nth-child(1) > div.post > "
        "div.single.postcon > div.readall-body > p")
    return "\n".join(x.text for x in selected[2:-3])


def decrypt(passage_content: str, encrypt_method: str):
    if encrypt_method == "none":
        return passage_content
    return passage_content.translate(str.maketrans(consts.charset, consts.dicts[encrypt_method]))


def detect_encrypt_method(passage_content: str):
    methods = dict()
    for method in consts.words:
        methods[method] = 0
        for word in consts.words[method]:
            if word in passage_content:
                methods[method] += consts.words[method][word]
    # for method, v in methods.items():
    #     s = sum(methods.values())
    #     print(method, v/s*100, "%")
    return max(methods, key=lambda x: methods[x])
