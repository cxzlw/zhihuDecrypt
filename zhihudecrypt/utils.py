from . import consts


def decrypt(passage_content: str, encrypt_method: str):
    if encrypt_method == "none":
        return passage_content
    return passage_content.translate(str.maketrans(consts.charset, consts.dicts[encrypt_method]))


def detect_encrypt_method_probability(passage_content: str):
    methods = dict()
    for method in consts.words:
        methods[method] = 0
        for word in consts.words[method]:
            if word in passage_content:
                methods[method] += consts.words[method][word]
    sum_num = sum(methods.values())
    if sum_num == 0:
        methods["none"] = 1
        sum_num = 1
    for method in methods:
        methods[method] /= sum_num
    return methods


def detect_encrypt_method(passage_content: str):
    probabilities = detect_encrypt_method_probability(passage_content)
    return max(probabilities, key=lambda x: probabilities[x])
